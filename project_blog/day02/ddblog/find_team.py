#小学春游 - 两组同学，每组1-3人，每组有一个队长;
# 春游期间，由于景点人数较多，秩序混乱，
# 班主任要求在指定地点，按组集合

#源数据 (与表中的记录的结构相似)
s = [{'name':'leader-1','belong_to':None},
     {'name':'jack','belong_to':'leader-2'},
     {'name':'lili','belong_to':'leader-1'},
     {'name':'leader-2','belong_to':None},
     {'name':'Tom', 'belong_to':'leader-1'}]
#目标数据(与json格式的结构相似)
d = [
    {'name':'leader-1', 'team':[{'name':'lili'},{'name':'Tom'}]},
    {'name':'leader-2', 'team':[{'name':'jack'}]}
]
# 将源数据s 作为data的实参,目标数据d作为返回值
def find_team(data):
    # 作为返回值
    leader_data=[]
    # 存储队员信息
    m_dict={}
    # 遍历源数据,区分队长和队员
    for d in s:
        if d['belong_to']:
            # 队员信息
            # 如果键不存在,调用函数设置
            # 如果键已经存在,该函数不执行
            m_dict.setdefault(d['belong_to'],[])
            m_dict[d['belong_to']].append({'name':d['name']})
        else:
            # 队长信息
            leader_data.append({'name':d['name'],'team':[]})
    print(m_dict)
    # 将队长信息和队员信息合二为一
    for l in leader_data:
        if l['name'] in m_dict:
            l['team']=m_dict[l['name']]
    return leader_data
if __name__ == '__main__':
    print(find_team(s))