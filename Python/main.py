from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import pandas as pd
import jieba
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import ast
from collections import Counter


app = FastAPI()


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  
  allow_credentials=True,
  allow_methods=["*"],  
  allow_headers=["*"],  
)



# 数据库操作（传入sql语句，返回查询结果）
def ConnectDB(sql):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            dbname = "nete",
            user = "postgres",
            password = "0623",
            host = "localhost",
            port = "5432"
        )
        cur = conn.cursor()
        cur.execute(sql)
        all_data = cur.fetchall()
        return all_data
    except Exception as e:
        print(e)
        return {'message':"Failed to get categories"}
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


# 图1
@app.get("/picture1")
async def picture1():
    data = ConnectDB("select * from scgm")
    year = [i[0] for i in data]
    value = [i[1] for i in data]
    values = [1.47]
    for i in value:
        values.append(i)
    zzl = []
    for i in range(1,len(values)):
        num = (values[i] - values[i-1]) / values[i-1]
        num = round(num*100,2)
        zzl.append(num)
    if year and value and zzl:
        return {"year": year, "value": value, "zzl": zzl}
    else:
        return {'message':"Data not found / Data is empty"}




# 图2
@app.get("/picture2")
async def picture2():
    type1 = ConnectDB("select industry from bosszp")
    type2 = ConnectDB("select industry from qcwy")
    type1_new = [i[0] for i in type1]
    type2_new = [i[0] for i in type2]
    for i in range(len(type2_new)):
        type2_new[i] = type2_new[i][2:-2]
    text = type1_new + type2_new
    text_new = []
    for sentence in text:
        text_new.append(cut_word(sentence))
    transform = CountVectorizer()
    data = transform.fit_transform(text_new)
    data_list = data.toarray()
    column_sum = np.sum(data_list, axis=0)
    feature_names = transform.get_feature_names_out()
    data_dict = dict(zip(list(feature_names), list(column_sum)))
    sorted_data = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))
    type_name = list(sorted_data.keys())
    type_data = list(sorted_data.values())
    print(type(type_name))
    for i in range(len(type_data)):
        type_data[i] = int(type_data[i])
    type_name = type_name[:10]
    type_data = type_data[:10]
    if type_name and type_data:
        return {"name": type_name, "value": type_data}
    else:
        return {'message':"Data not found / Data is empty"}
    

def cut_word(text):
    # print(" ".join(list(jieba.cut(text))))
    return " ".join(list(jieba.cut(text)))




# 图3
@app.get("/picture3")
async def picture3():
    data = ConnectDB("select skills from bosszp")
    # print(data)
    skill1 = [item[0] for item in data]
    skill1_new = [ast.literal_eval(i) for i in skill1]
    skill1_new = [item for sublist in skill1_new for item in sublist]
    text = skill1_new
    my_counter = Counter(text)
    data_dict = dict(list(my_counter.items()))
    sorted_data = dict(sorted(data_dict.items(), key=lambda item:item[1], reverse=True))
    data = sorted_data
    data = skillList(data)
    skill_name = list(data.keys())[0:20]
    skill_num = list(data.values())[0:20]
    sum_data = sum(skill_num)
    skill_show_value = [round(i/sum_data*100,2) for i in skill_num]
    print(skill_name)
    print(skill_show_value)
    if skill_name and skill_show_value:
        return {"name": skill_name, "value": skill_show_value}
    else:
        return {'message':"Data not found / Data is empty"}
    

def skillList(data):
    list = [
    'Java', 'MySQL', 'Python', 'Spring', '物联网', 'C++', 'Redis', 'C#', 
    'SpringCloud', 'IOT', 'MyBatis', 'Netty', 'Socket技术', 'iot', 'MongoDB', 
    'SQL Server', 'C语言', 'MQTT', '架构师', '后端开发', 'JavaScript', 'Nginx', 
    '微服务经验', 'PLC', 'MES开发经验', 'C端产品', 'CSS', 'Kafka', '分布式技术', 
    '大数据经验', 'Linux开发/部署经验', '大数据处理经验', '软件工程师', 'Golang', 
    '硬件测试', 'HTML5', '.NET开发经验', 'Docker', '计算机/软件工程相关专业', 
    '智能家居', 'Framework', 'Tomcat', 'Vue', '测试工作经验', 'Web测试经验', 
    'rust开发', 'IoT项目技术支持', 'APP测试', '编程', 'PC端', 'Windows', 'Maven', 
    'Eclipse', '人工智能', 'API接口开发', 'Web开发', '软件产品经理', '前端开发经验', 
    '数据结构', '通信', '软件测试', '消息队列', '高级软件工程师', 'ANDROID', 
    '安全技术', 'PHP', 'Rust', '编码技术', '硬件开发', '产品设计', 'IoT产品', 
    '物联网开发', '计算机网络', '数据库管理', '移动端开发', '软件开发', 'ERP产品', 
    'ERP开发经验', '嵌入式开发', '嵌入式技术', '自动化测试', '自动化', 'AI产品', 
    '物联网开发', 'AI/ML', '算法工程师', '系统架构师', '无人驾驶', '计算机视觉', 
    '虚拟现实', '嵌入式系统'
    ]
    my_dict = {}
    for key,value in data.items():
        if key in list:
            my_dict[key] = value
    return my_dict






# 图4
@app.get("/picture4")
async def picture4():
    data = get_china_data()
    province = list(data.keys())
    value = list(data.values())
    # print(province)
    # print(value)
    if province and value:
        return {"name": province, "value": value}
    else:
        return {'message':"Data not found / Data is empty"}
    

def deal_with_area(area):
    flag = False
    pos = None
    for i in range(len(area)):
        if(area[i]=='·'):
            pos = i
            flag = True
            break
    if flag:
        # print(area)
        area = area[0:pos]
    # print(area)
    return area


def all_provinces_in_china():
    all_provinces_in_china = [
    "河北省", "山西省", "辽宁省", "吉林省", "黑龙江省", "江苏省", "浙江省", "安徽省", "福建省", "江西省", "山东省",
    "河南省", "湖北省", "湖南省", "广东省", "海南省", "四川省", "贵州省", "云南省", "陕西省", "甘肃省", "青海省", "台湾省",
    "内蒙古自治区", "广西壮族自治区", "西藏自治区", "宁夏回族自治区", "新疆维吾尔自治区",
    "北京市", "天津市", "上海市", "重庆市",
    "香港特别行政区", "澳门特别行政区"
    ]
    return all_provinces_in_china



def all_cities_in_province():
    all_cities_in_province = {
        '广东省' : ["广州", "深圳", "清远", "韶关", "河源", "梅州", "潮州", "汕头",
                "揭阳", "汕尾", "惠州", "东莞", "珠海", "中山", "江门", "佛山",
                "肇庆", "云浮", "阳江", "茂名", "湛江"],
        '江苏省' : ["南京","徐州","连云港","宿迁","淮安","盐城","扬州","泰州","南通","镇江","常州","无锡","苏州"]
    }
    return all_cities_in_province


def city_in_province():
    # Define cities by province
    cities_by_province = {
        '江苏省': ['淮安', '徐州', '南京', '苏州', '南通', '常州', '无锡', '泰州', '连云港', '昆山', '常熟', '宿迁'],
        '湖南省': ['邵阳', '长沙', '衡阳', '湘西'],
        '宁夏回族自治区': ['吴忠'],
        '河南省': ['洛阳', '郑州', '南阳', '新乡', '开封', '商丘'],
        '四川省': ['成都', '资阳', '眉山', '绵阳'],
        '山东省': ['威海', '济南', '潍坊', '青岛', '烟台', '临沂', '聊城', '日照', '东营'],
        '广东省': ['东莞', '中山', '惠州', '佛山', '深圳', '珠海', '广州', '清远', '江门'],
        '云南省': ['昆明', '保山'],
        '浙江省': ['丽水', '台州', '杭州', '嘉兴', '温州', '金华', '宁波', '湖州', '绍兴'],
        '海南省': ['海口'],
        '江西省': ['南昌', '上饶', '九江'],
        '辽宁省': ['大连', '抚顺', '沈阳'],
        '北京市': ['北京'],
        '重庆市': ['重庆'],
        '陕西省': ['西安'],
        '福建省': ['厦门', '泉州', '福州'],
        '甘肃省': ['兰州'],
        '广西壮族自治区': ['南宁', '钦州', '桂林','柳州'],
        '山西省': ['上饶', '太原', '临汾', '大同'],
        '内蒙古自治区': ['呼和浩特'],
        '吉林省': ['长春'],
        '河北省': ['唐山', '沧州', '邯郸', '石家庄', '保定'],
        '新疆维吾尔自治区': ['乌鲁木齐'],
        '上海市':['上海'],
        '安徽省': ['合肥', '芜湖', '蚌埠'],
        '天津市': ['天津'],
        '湖北省':['武汉','襄阳'],
        '贵州省':['贵阳'],
        '黑龙江省':['哈尔滨']
    }
    return cities_by_province


def get_area():
    data_BossZP = ConnectDB("select area from bosszp")
    data_QCWY = ConnectDB("select area from qcwy")
    area1 = [i[0] for i in data_BossZP]
    area2 = [i[0] for i in data_QCWY]
    # print(area1)
    # print(area2)
    area2_new = []
    for i in range(len(area2)):
        if isinstance(area2[i], str):
            area2_new.append(area2[i])
    area2 = area2_new
    for i in range(len(area2)):
        area2[i] = deal_with_area(str(area2[i]))
    area = area1 + area2
    my_counter = Counter(area)
    area_dict = dict(list(my_counter.items()))
    area_new_dict = {}
    for key,value in area_dict.items():
        if key[-1]=='省':
            continue
        else:
            area_new_dict[key] = value
    return area_new_dict


def get_china_data():
    data = city_in_province()
    value = get_area()
    province_dict = {}
    for province,cities in data.items():
        sum = 0
        for city in cities:
            sum += value[city]
        province_dict[province] = sum
    province_new_dict = {}
    all_provinces = all_provinces_in_china()
    for province in all_provinces:
        province_new_dict[province] = 0
    for key,value in province_dict.items():
        if key in all_provinces:
            province_new_dict[key] = value
    province_dict = province_new_dict
    # print(province_dict)
    return province_dict



# 图5
@app.get("/picture5")
async def picture5():
    data = get_province_data('江苏')
    city = list(data.keys())
    value = list(data.values())
    print(city)
    print(value)
    if city and value:
        return {"name": city, "value": value}
    else:
        return {'message':"Data not found / Data is empty"}


def get_province_data(province_name):
    all_provinces = all_cities_in_province()[province_name+'省']
    province = city_in_province()[province_name+'省']
    value = get_area()
    province_data = {}
    for city in all_provinces:
        city += '市'
        province_data[city] = 0
    for city in province:
        num = value[city]
        city += '市'
        province_data[city] = num
    # print(province_data)
    return province_data


# 图6
@app.get("/picture6")
async def picture6():
    data = get_province_data('广东')
    city = list(data.keys())
    value = list(data.values())
    print(city)
    print(value)
    if city and value:
        return {"name": city, "value": value}
    else:
        return {'message':"Data not found / Data is empty"}



# 图7
@app.get("/picture7")
async def picture7():
    salary = get_QCWY_salary_data()
    s = pd.Series(salary)
    median_value = s.median()
    degree = get_QCWY_degree_data()
    order_degree = ['初中及以下','中技/中专','高中','大专','本科','硕士','博士']
    if salary and degree:
        return {'name':degree,'value':salary}



def deal_with_QCWY_salary_data(salary):
    salary_new = None
    if salary[-1]=='薪':
        salary = salary.split('·')[0]
        if salary[-1]=='千':
            salary_min = int(salary.split('-')[0])
            salary_max = int(salary.split('-')[1][0:-1])
            salary_new = (salary_min*1000+salary_max*1000)/2
            # print(salary_new)
        elif salary[-1]=='万':
            salary_min = salary.split('-')[0]
            salary_max = salary.split('-')[1]
            if salary_min[-1]=='千':
                salary_min = float(salary_min[0:-1])
                salary_max = float(salary_max[0:-1])
                salary_new = (salary_min*1000+salary_max*10000)/2
            else:
                salary_min = float(salary_min)
                salary_max = float(salary_max[0:-1])
                salary_new = (salary_min*10000+salary_max*10000)/2
    if salary[-1]=='万':
        salary_min = salary.split('-')[0]
        salary_max = salary.split('-')[1]
        if salary_min[-1]=='千':
            salary_min = float(salary_min[0:-1])
            salary_max = float(salary_max[0:-1])
            salary_new = (salary_min*1000+salary_max*10000)/2
        else:
            salary_min = float(salary_min)
            salary_max = float(salary_max[0:-1])
            salary_new = (salary_min*10000+salary_max*10000)/2
    elif salary[-1]=='千':
        salary_min = float(salary.split('-')[0])
        salary_max = float(salary.split('-')[1][0:-1])
        salary_new = (salary_min*1000+salary_max*1000)/2
        # print(salary_min,salary_max)
    elif salary[-1]=='年':
        salary = salary[0:-3]
        salary_min = int(salary.split('-')[0])
        salary_max = int(salary.split('-')[1])
        middle_salary = (salary_min+salary_max)/2
        salary_new = middle_salary/12*10000
        # print(salary_min,salary_max)
    # print(salary)
    return salary_new

def get_QCWY_salary_data():
    data = ConnectDB("select salary from qcwy")
    salary = [i[0] for i in data]
    # print(salary)
    salary_data = []
    for i in salary:
        # print(i)
        salary_data.append(deal_with_QCWY_salary_data(i))
    # print(salary_data)
    return salary_data

def get_QCWY_degree_data():
    data = ConnectDB("select degree from qcwy")
    degree = [i[0] for i in data]
    return degree

def get_QCWY_experience_data():
    data = ConnectDB("select year from qcwy")
    experience = [i[0] for i in data]
    return experience



# 图8
@app.get("/picture8")
async def picture8():
    salary = get_QCWY_salary_data()
    s = pd.Series(salary)
    median_value = s.median()
    experience = get_QCWY_experience_data()
    order_experience = ['无需经验','1年','1-2年','2年','1-3年','2-3年','3-4年',
                        '3-5年','3-6年','3-9年','4-6年','5-7年','5-8年','5-10年',
                        '8-9年','1年及以上','2年及以上','3年及以上','4年及以上',
                        '5年及以上','6年及以上','8年及以上','10年及以上']
    if salary and experience:
        return {'name':experience,'value':salary}






if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        app = "main:app",
        host = "127.0.0.1",
        port = 12345,
        reload = True,
        workers = 6
    )

