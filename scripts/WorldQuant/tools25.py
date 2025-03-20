import requests
from os import environ
from time import sleep
import time
import json
import pandas as pd
import random
import pickle
from itertools import product
from itertools import combinations
from collections import defaultdict
import pickle
import datetime
import traceback
from dotenv import load_dotenv
load_dotenv('.env')


ts_ops = ["ts_rank", "ts_zscore", "ts_delta",  "ts_sum", "ts_product",
          "ts_ir", "ts_std_dev", "ts_mean",  "ts_arg_min", "ts_arg_max", "ts_min_diff",
          "ts_max_diff", "ts_returns", "ts_scale", "ts_skewness", "ts_kurtosis",  
          "ts_quantile"]

# ts_rank(close,5)
def process_datafields(df, data_type):

    if data_type == "matrix":
        datafields = df[df['type'] == "MATRIX"]["id"].tolist()
    elif data_type == "vector":
        datafields = []

    tb_fields = []
    for field in datafields:
        tb_fields.append("winsorize(ts_backfill(%s, 120), std=4)"%field)
    return tb_fields


def process_datafields_opt(df, data_type):

    if data_type == "matrix":
        datafields = df[df['type'] == "MATRIX"]["id"].tolist()
    elif data_type == "vector":
        datafields = []

    call_opt=[]
    mean_opt=[]
    for opt in datafields:
        if "call" in opt:
            call_opt.append(opt)
        elif "mean" in opt:
            mean_opt.append(opt)

    tb_fields = []
    # for field in datafields:
    for call_opt_temp in call_opt:
        for mean_opt_temp in mean_opt:
            tb_fields.append(fr"winsorize(ts_backfill({call_opt_temp}/{mean_opt_temp}, 120), std=4)")
    return tb_fields

def login():
    username=environ.get('wq_account')
    password=environ.get('wq_password')
    s = requests.Session()
    s.auth = (username, password)
    response = s.post('https://api.worldquantbrain.com/authentication')
    print(response.content)
    return s  
 
def get_datafields(
    s,
    instrument_type: str = 'EQUITY',
    region: str = 'USA',
    delay: int = 1,
    universe: str = 'TOP3000',
    dataset_id: str = '',
    search: str = ''
):
    if len(search) == 0:
        url_template = "https://api.worldquantbrain.com/data-fields?" +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50" +\
            "&offset={x}"
        count = s.get(url_template.format(x=0)).json()['count'] 
        
    else:
        url_template = "https://api.worldquantbrain.com/data-fields?" +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&limit=50" +\
            f"&search={search}" +\
            "&offset={x}"
        count = 100
    
    datafields_list = []
    for x in range(0, count, 50):
        datafields = s.get(url_template.format(x=x))
        datafields_list.append(datafields.json()['results'])
 
    datafields_list_flat = [item for sublist in datafields_list for item in sublist]
 
    datafields_df = pd.DataFrame(datafields_list_flat)
    return datafields_df
 

 
def ts_factory(op, field):
    output = []
    #days = [3, 5, 10, 20, 60, 120, 240]
    days = [5, 22, 66, 120, 240]
    
    for day in days:
    
        alpha = "%s(%s, %d)"%(op, field, day)
        output.append(alpha)
    
    return output

def get_ops(s):
    # s=s_ll
    # 获取ops
    url="https://api.worldquantbrain.com/operators"
    res=s.get(url)
    # print(res.json())
    df = pd.DataFrame(res.json())
    return df

def get_first_order(vec_fields, ts_ops,prefix):
    print(ts_ops)
    alpha_set = []
    #for field in fields:
    if prefix:
        res_fields=[]
        for field in vec_fields:
            if prefix in field:
                res_fields.append(field)
    else:
        res_fields=vec_fields
    
    for field in res_fields:
        #reverse op does the work
        alpha_set.append(field)
        #alpha_set.append("-%s"%field)
        for op in ts_ops:
            if op.startswith("ts_") or op == "inst_tvr":
                alpha_set += ts_factory(op, field)
            else:
                alpha = "%s(%s)"%(op, field)
                alpha_set.append(alpha)
 
    return alpha_set

def intersection_of_lists(list1, list2):
    return [element for element in list1 if element in list2]


def generate_sim_data_single(alpha,decay, region, uni, neut):

    simulation_data = {
        'type': 'REGULAR',
        'settings': {
            'instrumentType': 'EQUITY',
            'region': region,
            'universe': uni,
            'delay': 1,
            'decay': decay,
            'neutralization': neut,
            'truncation': 0.08,
            'pasteurization': 'ON',
            'unitHandling': 'VERIFY',
            'nanHandling': 'ON',
            'language': 'FASTEXPR',
            'visualization': False,
        },
        'regular': alpha}


    return simulation_data


def single_simulate(alpha_lst, neut, region, universe, start):

    s = login()

    brain_api_url = 'https://api.worldquantbrain.com'

    x=0
    # progress_urls=[]
    for alpha, decay in alpha_lst:
        simulation_progress_url=''
        x+=1
        if x < start: continue

        sim_data = generate_sim_data_single(alpha,decay,region, universe, neut)
        try:
            simulation_response = s.post('https://api.worldquantbrain.com/simulations', json=sim_data)
            simulation_progress_url = simulation_response.headers['Location']
        except:
            print(" loc key error")
            sleep(600)
            s = login()

        print(fr"{x} post done")

        if simulation_progress_url:
            try:
                while True:
                    simulation_progress = s.get(simulation_progress_url)
                    if simulation_progress.headers.get("Retry-After", 0) == 0:
                        break
                    #print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
                    sleep(float(simulation_progress.headers["Retry-After"]))

                status = simulation_progress.json().get("status", 0)
                if status != "COMPLETE":
                    print("Not complete : %s"%(simulation_progress_url))

                """
                #alpha_id = simulation_progress.json()["alpha"]
                children = simulation_progress.json().get("children", 0)
                children_list = []
                for child in children:
                    child_progress = s.get(brain_api_url + "/simulations/" + child)
                    alpha_id = child_progress.json()["alpha"]

                    set_alpha_properties(s,
                            alpha_id,
                            name = "%s"%name,
                            color = None,)
                """
            except KeyError:
                print("look into: %s"%simulation_progress_url)
            except:
                print("other")


        print(fr"{x} simulate done")

    print("Simulate done")

def list_chuckation(field_list, num):
    list_chucked = []
    lens = len(field_list)
    i = 0
    while i+num <= lens:
        list_chucked.append(field_list[i:i+num])
        i += num
    list_chucked.append(field_list[i:lens])
    return list_chucked

def set_alpha_properties(
    s,
    alpha_id,
    name: str = None,
    color: str = None,
    selection_desc: str = "None",
    combo_desc: str = "None",
    tags: str = ["ace_tag"],
):
    """
    Function changes alpha's description parameters
    """
 
    params = {
        "color": color,
        "name": name,
        "tags": tags,
        "category": None,
        "regular": {"description": None},
        "combo": {"description": combo_desc},
        "selection": {"description": selection_desc},
    }
    response = s.patch(
        "https://api.worldquantbrain.com/alphas/" + alpha_id, json=params
    )



def get_fields_all():
    s=login()
    cat_list = ["analyst", "earnings", "fundamental", "", "insiders", "institutions", "macro", "model", "news", "option", "other", "pv", "risk", "sentiment", "shortinterest", "socialmedia"]
    region,universe=("USA","TOP3000")
    df_fields_ll=pd.DataFrame()
    for category in cat_list:
        datasets_df=get_datasets(s,region,category,universe,delay=1)  # 获取datasets
        # datasets_df
        # break
        if len(datasets_df)>0:
            dataset_id_lst=datasets_df["id"].tolist()      # 筛选后的dataset_id列表
        else:
            dataset_id_lst=[]
            # print(category)
        for dataset_id in dataset_id_lst:
            df = get_datafields(s, dataset_id = dataset_id, region=region, universe=universe, delay=1)
            # print(df)
            df_fields_ll=pd.concat((df_fields_ll,df),ignore_index=True)
            # print(len(df_fields_ll))
    fields_all_lst=df_fields_ll['id'].to_list()
    
    return fields_all_lst
    
def group_factory(op, field, region,flst):
    output = []
    vectors = ["cap"] 
    

    usa_group_13 = ['pv13_h_min2_3000_sector','pv13_r2_min20_3000_sector','pv13_r2_min2_3000_sector',
                    'pv13_r2_min2_3000_sector', 'pv13_h_min2_focused_pureplay_3000_sector']
    
    usa_group_1 = ['sta1_top3000c50','sta1_allc20','sta1_allc10','sta1_top3000c20','sta1_allc5']
    
    usa_group_2 = ['sta2_top3000_fact3_c50','sta2_top3000_fact4_c20','sta2_top3000_fact4_c10']
    
    usa_group_3 = ['sta3_2_sector', 'sta3_3_sector', 'sta3_news_sector', 'sta3_peer_sector',
                   'sta3_pvgroup1_sector', 'sta3_pvgroup2_sector', 'sta3_pvgroup3_sector', 'sta3_sec_sector']
    
    usa_group_4 = ['rsk69_01c_1m', 'rsk69_57c_1m', 'rsk69_02c_2m', 'rsk69_5c_2m', 'rsk69_02c_1m',
                   'rsk69_05c_2m', 'rsk69_57c_2m', 'rsk69_5c_1m', 'rsk69_05c_1m', 'rsk69_01c_2m']
    
    usa_group_5 = ['anl52_2000_backfill_d1_05c', 'anl52_3000_d1_05c', 'anl52_3000_backfill_d1_02c', 
                   'anl52_3000_backfill_d1_5c', 'anl52_3000_backfill_d1_05c', 'anl52_3000_d1_5c']
    
    usa_group_6 = ['mdl10_group_name']
    
    usa_group_7 = ['oth171_region_sector_long_d1_sector', 'oth171_region_sector_short_d1_sector', 
                   'oth171_sector_long_d1_sector', 'oth171_sector_short_d1_sector']
    
    usa_group_8 = ['oth455_competitor_n2v_p10_q50_w1_kmeans_cluster_10',
                     'oth455_customer_n2v_p10_q50_w5_kmeans_cluster_10',
                     'oth455_relation_n2v_p50_q200_w5_kmeans_cluster_20',
                     'oth455_competitor_n2v_p50_q50_w3_kmeans_cluster_10', 
                     'oth455_relation_n2v_p50_q50_w3_pca_fact2_cluster_10', 
                     'oth455_partner_n2v_p10_q50_w2_pca_fact2_cluster_5',
                     'oth455_customer_n2v_p50_q50_w3_kmeans_cluster_5',
                     'oth455_competitor_n2v_p50_q200_w5_kmeans_cluster_20']
    

    group_3 = ["oth171_region_sector_long_d1_sector", "oth171_region_sector_short_d1_sector",
               "oth171_sector_long_d1_sector", "oth171_sector_short_d1_sector"]
    
    bps_group = "bucket(rank(fnd28_value_05480/close), range='0.2, 1, 0.2')"
    cap_group = "bucket(rank(cap), range='0.1, 1, 0.1')"
    sector_cap_group = "bucket(group_rank(cap,sector),range='0,1,0.1')"

    
    groups = ["market","sector", "industry", "subindustry", bps_group, cap_group, sector_cap_group]

    if region == "usa":
        groups += usa_group_13 + usa_group_1 + usa_group_2 + usa_group_3 + usa_group_4 + usa_group_8 + group_3 
        groups += usa_group_5 + usa_group_6 + usa_group_7

    # flst=get_fields_all()
    groups=intersection_of_lists(flst,groups)
    for group in groups:
        if op.startswith("group_vector"):
            for vector in vectors:
                alpha = "%s(%s,%s,densify(%s))"%(op, field, vector, group)
                output.append(alpha)
        elif op.startswith("group_percentage"):
            alpha = "%s(%s,densify(%s),percentage=0.5)"%(op, field, group)
            output.append(alpha)
        else:
            alpha = "%s(%s,densify(%s))"%(op, field, group)
            output.append(alpha)
        
    return output



def get_datasets(s,region,category,universe,delay=1):
    url=fr"https://api.worldquantbrain.com/data-sets?category={category}&delay={delay}&instrumentType=EQUITY&limit=20&offset=0&region={region}&universe={universe}"
    
    response = s.get(url)
    datasets_list = []
    
    try:
        count=int(response.json()["count"])
        for i in range(0, count, 20):
            print(i)
            url=fr"https://api.worldquantbrain.com/data-sets?category={category}&delay={delay}&instrumentType=EQUITY&limit=20&offset={i}&region={region}&universe={universe}"
            response = s.get(url)
       
            datasets_list.append(response.json()['results'])

    except:
            print("finished re-login")
            # s = login()
            traceback.print_exc()

    datasets_list_flat = [item for sublist in datasets_list for item in sublist]
 
    datafields_df = pd.DataFrame(datasets_list_flat)
    return datafields_df

def get_datafields(
    s,
    instrument_type: str = 'EQUITY',
    region: str = 'USA',
    delay: int = 1,
    universe: str = 'TOP3000',
    dataset_id: str = '',
    search: str = ''
):
    if len(search) == 0:
        url_template = "https://api.worldquantbrain.com/data-fields?" +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50" +\
            "&offset={x}"
        count = s.get(url_template.format(x=0)).json()['count'] 
        
    else:
        url_template = "https://api.worldquantbrain.com/data-fields?" +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&limit=50" +\
            f"&search={search}" +\
            "&offset={x}"
        count = 100
    
    datafields_list = []
    for x in range(0, count, 50):
        datafields = s.get(url_template.format(x=x))
        datafields_list.append(datafields.json()['results'])
 
    datafields_list_flat = [item for sublist in datafields_list for item in sublist]
 
    datafields_df = pd.DataFrame(datafields_list_flat)
    return datafields_df


def get_group_second_order_factory(first_order, group_ops, region,flst):
    second_order = []
    for fo in first_order:
        for group_op in group_ops:
            second_order += group_factory(group_op, fo, region,flst)
    return second_order


def prune(next_alpha_recs, region, prefix, keep_num):
    # prefix is the datafield prefix, fnd6, mdl175 ...
    # keep_num is the num of top sharpe same-datafield alpha
    output = []
    num_dict = defaultdict(int)
    for rec in next_alpha_recs:
        exp = rec[1]
        field = exp.split(prefix)[-1].split(",")[0]
        sharpe = rec[2]
        if sharpe < 0:
            field = "-%s"%field
        if num_dict[field] < keep_num:
            num_dict[field] += 1
            decay = rec[-1]
            exp = rec[1]
            output.append([exp,decay])
    output_dict = {region : output}
    return output_dict

def get_alphas(start_date, end_date, sharpe_th, fitness_th, region, alpha_num, usage):
    s = login()
    next_alphas = []
    decay_alphas = []
    # 3E large 3C less
    count = 0
    for i in range(0, alpha_num, 100):
        print(i)
        url_e = "https://api.worldquantbrain.com/users/self/alphas?limit=100&offset=%d"%(i) \
                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \
                + "T00:00:00-04:00&dateCreated%3C2025-" + end_date \
                + "T00:00:00-04:00&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \
                + str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false&type!=SUPER"
        url_c = "https://api.worldquantbrain.com/users/self/alphas?limit=100&offset=%d"%(i) \
                + "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=2025-" + start_date  \
                + "T00:00:00-04:00&dateCreated%3C2025-" + end_date \
                + "T00:00:00-04:00&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \
                + str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false&type!=SUPER"
        urls = [url_e]
        if usage != "submit":
            urls.append(url_c)
        for url in urls:
            response = s.get(url)
            #print(response.json())
            try:
                alpha_list = response.json()["results"]
                #print(response.json())
                for j in range(len(alpha_list)):
                    alpha_id = alpha_list[j]["id"]
                    name = alpha_list[j]["name"]
                    dateCreated = alpha_list[j]["dateCreated"]
                    sharpe = alpha_list[j]["is"]["sharpe"]
                    fitness = alpha_list[j]["is"]["fitness"]
                    turnover = alpha_list[j]["is"]["turnover"]
                    margin = alpha_list[j]["is"]["margin"]
                    longCount = alpha_list[j]["is"]["longCount"]
                    shortCount = alpha_list[j]["is"]["shortCount"]
                    decay = alpha_list[j]["settings"]["decay"]
                    exp = alpha_list[j]['regular']['code']
                    count += 1
                    #if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):
                    if (longCount + shortCount) > 100:
                        if sharpe < -1.2:
                            exp = "-%s"%exp
                        rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]
                        print(rec)
                        if turnover > 0.7:
                            rec.append(decay*4)
                            decay_alphas.append(rec)
                        elif turnover > 0.6:
                            rec.append(decay*3+3)
                            decay_alphas.append(rec)
                        elif turnover > 0.5:
                            rec.append(decay*3)
                            decay_alphas.append(rec)
                        elif turnover > 0.4:
                            rec.append(decay*2)
                            decay_alphas.append(rec)
                        elif turnover > 0.35:
                            rec.append(decay+4)
                            decay_alphas.append(rec)
                        elif turnover > 0.3:
                            rec.append(decay+2)
                            decay_alphas.append(rec)
                        else:
                            next_alphas.append(rec)
            except:
                print("%d finished re-login"%i)
                s = login()

    output_dict = {"next" : next_alphas, "decay" : decay_alphas}
    print("count: %d"%count)
    return output_dict


def simulate(alpha_dict, region_dict, name, neut, start, stone_bag):
    s = login()
 
    #random.shuffle(alpha_set)
    #regions = [("USA", "TOP3000")]
    #stone_bag = []
 
    for key, alpha_set in alpha_dict.items():
        print("curr %s len %d"%(key, len(alpha_set)))
        groups = list_chuckation(alpha_set,3)
        for idx, group in enumerate(groups):
            if idx < start: continue
            region, uni = region_dict[key]
            progress_urls = []
            for field, decay in group:
                #alpha = "rank(vec_avg(%s))"%(field)
                #alpha = "%s+%s"%(field, recipe)
                alpha = "%s"%(field)
                print("group %d %s %s %s %s"%(idx, alpha, region, uni, decay))
                simulation_data = {
                        'type': 'REGULAR',
                        'settings': {
                            'instrumentType': 'EQUITY',
                            'region': region, 
                            'universe': uni, 
                            'delay': 1,
                            'decay': decay, 
                            'neutralization': neut,
                            #'neutralization': 'COUNTRY',
                            #'neutralization': 'SECTOR',
                            #'neutralization': 'MARKET',
                            'truncation': 0.08,
                            'pasteurization': 'ON',
                            'unitHandling': 'VERIFY',
                            'nanHandling': 'ON',
                            'language': 'FASTEXPR',
                            'visualization': False,
                            "testPeriod": "P0D",
                        },
                        'regular': alpha}
                try:
                    simulation_response = s.post('https://api.worldquantbrain.com/simulations', json=simulation_data)
                    print(simulation_response.status_code)
                    simulation_progress_url = simulation_response.headers['Location']
                    progress_urls.append(simulation_progress_url)
                except KeyError:
                    print(" loc key error")
                    sleep(600)
                    s = login()
                except:
                    print("1")
                    sleep(600)
                    s = login()
                    
            print("group %d post done"%(idx))
            print(fr"{datetime.datetime.now()}------------------")
            for progress in progress_urls:
                while True:
                    simulation_progress = s.get(progress)
                    if simulation_progress.headers.get("Retry-After", 0) == 0:
                        break
                    #print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
                    sleep(float(simulation_progress.headers["Retry-After"]))
 
                print("%s done simulating, getting alpha details"%(progress))
                try:
                    alpha_id = simulation_progress.json()["alpha"]
 
                    set_alpha_properties(s, 
                            alpha_id,
                            name = "%s"%name,
                            color = None,)
 
                    stone_bag.append(alpha_id)
 
                except KeyError:
                    print("look into: %s"%progress)
                except:
                    print("other")
 
 
            print("group %d %s simulate done"%(idx, region))
 
    print("stones:" )
    print(len(stone_bag))
    #print("success rate: %.3f"%(float(len(stone_bag2))/len(comb_fields)))
    return stone_bag






def get_check_submission(s, alpha_id):
    """
    Function gets alpha's check submission checks
    and returns result in dataframe
    """

    while True:
        result = s.get("https://api.worldquantbrain.com/alphas/" + alpha_id + "/check")
        if "retry-after" in result.headers:
            time.sleep(float(result.headers["Retry-After"]))
        else:
            break
    try:
        if result.json().get("is", 0) == 0:
            return pd.DataFrame()

        checks_df = pd.DataFrame(
                result.json()["is"]["checks"]
        )

        pc = checks_df[checks_df.name == "SELF_CORRELATION"]["value"].values[0]

        if not any(checks_df["result"] == "FAIL"):
            return pc

        else:
            return -2
    except:
        print("catch: %s"%(alpha_id))
        return "collect"


def get_timenow():

    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")







def check_submission(alpha_bag, gold_bag, start):
    depot = []
    s = login()
    for idx, g in enumerate(alpha_bag):
        if idx < start:
            continue
        if idx % 5 == 0:
            print(idx)
        #print(idx)
        pc = get_check_submission(s, g)
        if pc != -2:
            print(g)
            gold_bag.append((g, pc))
        elif pc == "collect":
            print("sleep 600")
            sleep(600)
            s = login()
            depot.append(g)
    print(depot)
    return gold_bag

if __name__=="__main__":
    pc_fields=['test']
    first_order = get_first_order(pc_fields, ts_ops)