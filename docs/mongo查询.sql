/* mongo表中的字段c_hlab_teacher_info_rt
w5_t2:0
merit_cnt_1:0
teach_ks:120
update_full_teacher_time:2020-08-13 14:26:34
*/

-- 查看mongo版本
db.version();

--  查询 的执行计划
db.c_trial_course_tch_feature.find().explain()

db.c_trial_course_tch_feature.find({'teacher_id':{$eq:382151}}).explain()

-- mongo创建索引与联合索引  3.x版本以后 只有.createIndex(), .ensureIndex()作为.createIndex()的别名
db.test.ensureIndex({name:1},{name:'index_name'})  -- mongo版本4.2以后, 默认使用background, 如果不需要可以指定false
db.test.ensureIndex({name:1,age:1,sex:1},{name:'index_nas'})

-- 单字段索引的升降序无所谓，合理使用可以提高联合索引的效率

-- 创建稀疏索引
db.getCollection("c_alb_course_schedule_log_meta").ensureIndex({"arrange_course_schedule_id": -1}, {sparse:true, background:true})



-- 创建唯一索引
db.getCollection("c_alb_course_schedule_log_meta").ensureIndex({"arrange_course_schedule_id": -1}, {unique:true, background:true})

-- 同一个字段分开创建不同类型的索引是多个索引，如果想加多个属性，应该一起创建，如：{unique:true, sparse:true, background:true}
-- background:true 当集合中已有数据时应加该参数，避免阻塞其他操作 
-- {"arrange_course_schedule_id": -1} 1和-1指升降序

-- mongo查询时使用索引 是根据创建 的时候从左到右依次进行的，所以假设只创建了复合索引，查询时只查单一字段 也是 有效的

-- mongo查看已有索引
db.c_hlab_teacher_info_rt.getIndexes()

-- mongo修改索引：只能先删除再创建

-- mongo删除指定索引
db.c_alb_course_schedule_log_meta.dropIndex({ "arrange_course_schedule_id": 1})


-- mongo删除全部索引
db.c_alb_course_schedule_log_meta.dropIndexes()

-- mongo query
db.c_hlab_teacher_info_rt.find({},
{'teaching_style':1,'teacher_id':1}
).count()  -- 62048

-- teaching_style character 字段值没有同步到mongo
db.c_hlab_teacher_info_rt.find({
    'teaching_style': {
        $exists:true
    }
}
,{'teaching_style':1,'teacher_id':1}
)

db.c_hlab_teacher_info_rt.find({
    'character': {
        $exists:true
    }
}
,{'character':1,'teacher_id':1}
).limit(20)

-- trail_success_cnt_100 
db.c_hlab_teacher_info_rt.find({
    'trail_success_cnt_100': {
        $exists:true
    }
}
,{'trail_success_cnt_100':1,'teacher_id':1}
).limit(20)

db.c_hlab_teacher_info_rt.find({
    'trail_success_cnt_100': {
        $exists:true
    }
}
,{'trail_success_cnt_100':1,'teacher_id':1}
).count()

-- 查看新增字段：create_time tr_local_label tr_local_city_lst
db.c_hlab_teacher_info_rt.find({
    'create_time': {
        $exists:true
    }
	,'tr_local_label': {
        $exists:true
    }
	,'tr_local_city_lst': {
        $nin:[-1]
    }
}
,{'teacher_id':1,'create_time':1,'tr_local_label':1,'tr_local_city_lst':1}
).limit(20)

-- 新建collection
db.createCollection("c_alb_ta_base_info")
-- 插入数据
db.c_alb_ta_base_info.insertMany([{"ta_id":12358,"ta_city_id":51},{"ta_id":12,"ta_city_id":360}])
db.c_alb_ta_base_info.insertMany([{"ta_id":58,"ta_city_id":12}])
-- 更新数据  120 35696 98871 老师需要新增几个字段：create_time tr_local_label tr_local_city_lst
db.c_hlab_teacher_info_rt.update({"teacher_id":120},{$set:{'create_time':'2020-07-01','tr_local_label':1,'tr_local_city_lst':[51]}},{upsert:true})
db.c_hlab_teacher_info_rt.update({"teacher_id":35696},{$set:{'create_time':'2020-05-12','tr_local_label':1,'tr_local_city_lst':[51]}})
db.c_hlab_teacher_info_rt.update({"teacher_id":98871},{$set:{'create_time':'2020-02-05','tr_local_label':1,'tr_local_city_lst':[12]}})

db.c_hlab_teacher_info_rt.update({"teacher_id":98871},{$set:{'trf_rate':'0.48','trial_course_total_cnt':100}})

-- 查看线上返回数据
db.c_alb_course_schedule_log_meta.find().sort({'arrange_course_schedule_id':-1}).limit(20)

-- $or $elemMatch 
db.c_hlab_teacher_info_rt.aggregate({'$or': [{'$elemMatch': {'merit_cnt_1': {'$eq': '0'},'w5_t2':{'$eq': '0'}}},{'$elemMatch': {'teach_ks': {'$lt': '10'}}}]}
,{'$project':{'teacher_id':1, 'merit_cnt_1':1, 'w5_t2':1, 'teach_ks':1}}
).limit(20)

db.c_hlab_teacher_info_rt.aggregate({'$match': {'merit_cnt_1': {'$eq': '0'},'w5_t2':{'$eq': 5}}}
,{'$project':{'teacher_id':1, 'merit_cnt_1':1, 'w5_t2':1, 'teach_ks':1}}
).limit(20)


db.c_hlab_teacher_info_rt.aggregate({'$match': {'$or': [{'merit_cnt_1': {'$eq': '0'},'w5_t2':{'$eq': 5}}, {'teach_ks': {'$lt': '10'}}]}}
,{'$project':{'teacher_id':1, 'merit_cnt_1':1, 'w5_t2':1, 'teach_ks':1}}
).limit(20)

-- 实现if a and b else 


-- 修改mongo集合的所有字段类型
db.c_alb_course_schedule_log_meta.find().forEach( function (x) {
 x.update_time = new ISODate(x.update_time);
  db.c_alb_course_schedule_log_meta.save(x);
});

-- 指定记录的字段类型
db.getCollection('c_alb_course_schedule_log_meta').updateOne({_id: ObjectId("5ef84f6a15bb8bd58a420077")},{$set: {update_time: new Date("2010-01-01 00:00:00")}})

"synState":"2010-01-01 00:00:00"

-- shell mongo 连接 在180.23
shell: mongo bisvc-1.mongodb.idc.cedu.cn:27017/qq_pool_score

mongo: use qq_pool_score

mongo: db.c_alb_course_schedule_log_meta.find({}).projection({}).sort({_id:-1}).limit(10)

-- 根据数据类型筛选返回结果  2 字符串 17 时间戳 9 date
db.c_alb_course_schedule_log_meta.find({'update_time':{$type:2}}).count()

db.getCollection('c_alb_course_schedule_log_meta').updateOne({_id: ObjectId("5f923a3015bb8bd58a8df785")},{$set: {update_time: new Date("2020-10-23 10:04:32")}})

-- 修改mongo集合中符合条件的文档中的字段类型
db.c_alb_course_schedule_log_meta.find({'update_time':{$gte:'2020-10-23 00:00:00'}}).forEach( function (x) { x.update_time = new ISODate(x.update_time);db.c_alb_course_schedule_log_meta.save(x);});

-- 字符串日期修改为date
db.c_alb_course_schedule_log_meta.find({'update_time':{$type:2}}).forEach( function (x) { x.update_time = new ISODate(x.update_time);db.c_alb_course_schedule_log_meta.save(x);});


-- 日期比较
db.c_alb_course_schedule_log_meta.find({
    'update_time': {
        $gte:ISODate('2020-10-13 00:00:00')
    }
}
,{}
).count()

db.c_alb_course_schedule_log_meta.find({
    '$and':[
    {'update_time': {
        $gte:ISODate('2020-10-23 00:00:00')
    }},
    {'update_time':{$type:9}}
    ]
}
,{}
).sort({update_time:-1}).limit(100)

-- 字段排序
db.c_alb_course_schedule_log_meta.find({'update_time':{$type:9}}).sort({'update_time':1}).limit(100)

-- 查看某一字段重复次数 只用改 clounm_name 就行
db.getCollection('c_hlab_teacher_info_rt').aggregate( 
{'$group':{
        '_id': {'clounm_name': '$clounm_name'},
        'uniqueIds': {'$addToSet': '$_id'},
        'count' : {'$sum': 1}
    }},
    {'$match': {
        'count': {'$gt': 1}
    }}
)

-- 删除集合
db.collection_name.drop()

-- 删除集合中的文档
db.c_assistant_teacher_test_feature.deleteMany({'ta_tch_id':{$eq:null}})

-- 删除文档中的一个域 multi为true表示更新所有满足要求的文档
db.c_hlab_teacher_info_rt.update({teacher_id:{$eq:370500}}, {$unset: {grade_list: 1}}, {multi: true})

-- 把集合中的某些数据复制到另一个表中
1、先把表中数据全部复制到另一个表中:  db.source_collection_name.find().forEach(function(x){db.target_collection_name.insert(x)})
2、按条件删除新表中的数据:  db.target_collection_name.deleteMany({'grade_list':{$exists:true}})


--mongo关键字
$elemMatch 
对于数组字段
"relatives" : [ 
        {
            "name" : "赵刚",
            "relationship" : 0
        }, 
        {
            "name" : "秀英",
            "relationship" : 1
        }
    ]
，使用find查找 .find({"relatives.name": "赵刚", "relatives.relationship": 2}), 每个查询条件只要满足数组中有一项条件，而不需要一项满足所有条件
但是elemMatch可以找到数组中存在 一项满足所有条件的记录：.find({"relatives":{"$elemMatch":{"name": "赵刚", "relationship": 0}}})




-- pymongo
import pandas as pd 
import json 
from pymongo import MongoClient
host = ['bisvc-1.mongodb.idc.cedu.cn', 'bisvc-2.mongodb.idc.cedu.cn', 'bisvc-3.mongodb.idc.cedu.cn']
port = 27017
db = 'qq_pool_score'
dbclient = MongoClient(
        host=host,
        port=port
)

tch_db = dbclient.qq_pool_score.c_hlab_teacher_info_rt

list(tch_db.find({"teaching_style":{"$exists": True}},{"teaching_style":1,"teacher_id":1}))[:2]


# pipe_candidata_pool_info_1 = {'$project':{'teacher_id': 1, 'enroll_time':1}}


train_data = [{'teacher_id': 180104, 'bi_match_score': 0.1222705341}, {'teacher_id': 206841, 'bi_match_score': 0.1258978942}]

train_data = pd.DataFrame(train_data)

train_data = json.loads(train_data.to_json(orient='records'))

a = list(tch_db.aggregate([{'$match':{"teacher_id": {"$in": train_data['teacher_list']}}},{'$project':{'teacher_id': 1, 'enroll_time':1}}]))

tch_db.find_one({"update_time":{"$exists": True}},{'arrange_course_schedule_id':1})

-- 查询已有索引
list(tch_db.list_indexes())

-- 新建集合
my_db = dbclient.qq_pool_score.c_hlab_student_info_rt

-- 新建索引
my_db.create_index([('student_id',1)], unique = True, background = True)

-- 删除文档
my_db.delete_many({'ta_tch_id':{'$eq':None}})


-- 常用mongo查询语句
-- 查看直排项目最新日志
trial_log_collection = dbclient.qq_pool_score.c_alb_course_schedule_log_meta
-- projection 中的字段若是只指定了False，那其他字段就会全部显示；如果有False有True, 那就只显示为True的字段 
result = trial_log_collection.find({}, projection={"_id": False}).limit(1).sort([("update_time",-1)])
list(result)

--  在线课质检日志查看
eva_log_collection = dbclient.qq_pool_score.c_alb_tch_stu_evaluate_service_log
result = eva_log_collection.find({}, projection={"_id": False}).limit(1).sort([("update_time",-1)])
list(result)


