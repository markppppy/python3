## alpha 模板和 alpha_template_id 的 映射关系
- alpha_template_id
  - template 

### alpha_template_1
- group_rank(ts_rank({fundamental model data}, 252), industry) 
- 用过的数据集id
  - fundamental6
  - option9
  - analyst4 
  - 



### alpha_template_2 

```
a = ts_zscore({datafield}, 252);
a1 = group_neutralize(a, bucket(rank(cap), range='0.1,1,0.1'));
a2 = group_neutralize(a1, industry);b = ts_zscore(cap, 252);
b1 = group_neutralize(b, industry);c = regression_neut(a2,b1);
c
```

