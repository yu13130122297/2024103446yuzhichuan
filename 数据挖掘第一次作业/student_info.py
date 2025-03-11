class Student:
    def __init__(self, student_id, name, gender, address, phone, email):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.address = address
        self.phone = phone
        self.email = email

def create_tuple_student_list():
    # 创建包含5个学生信息的元组列表
    students = [
        ("001", "张三", "男", "北京市海淀区", "13800138000", "zhangsan@email.com"),
        ("002", "李四", "女", "上海市浦东新区", "13900139000", "lisi@email.com"),
        ("003", "王五", "男", "广州市天河区", "13700137000", "wangwu@email.com"),
        ("004", "赵六", "女", "深圳市南山区", "13600136000", "zhaoliu@email.com"),
        ("005", "孙七", "男", "成都市武侯区", "13500135000", "sunqi@email.com")
    ]
    return students

def create_list_student_info():
    # 创建包含学生信息的列表
    students = [
        ["001", "张三", "男", "北京市海淀区", "13800138000", "zhangsan@email.com"],
        ["002", "李四", "女", "上海市浦东新区", "13900139000", "lisi@email.com"],
        ["003", "王五", "男", "广州市天河区", "13700137000", "wangwu@email.com"],
        ["004", "赵六", "女", "深圳市南山区", "13600136000", "zhaoliu@email.com"],
        ["005", "孙七", "男", "成都市武侯区", "13500135000", "sunqi@email.com"]
    ]
    return students

def create_dict_student_info():
    # 创建包含学生信息的字典
    students = {
        "001": {"name": "张三", "gender": "男", "address": "北京市海淀区", "phone": "13800138000", "email": "zhangsan@email.com"},
        "002": {"name": "李四", "gender": "女", "address": "上海市浦东新区", "phone": "13900139000", "email": "lisi@email.com"},
        "003": {"name": "王五", "gender": "男", "address": "广州市天河区", "phone": "13700137000", "email": "wangwu@email.com"},
        "004": {"name": "赵六", "gender": "女", "address": "深圳市南山区", "phone": "13600136000", "email": "zhaoliu@email.com"},
        "005": {"name": "孙七", "gender": "男", "address": "成都市武侯区", "phone": "13500135000", "email": "sunqi@email.com"}
    }
    return students

def main():
    # 1. 用tuple存储学生信息
    tuple_students = create_tuple_student_list()
    print("=== 元组存储的学生信息 ===")
    for student in tuple_students:
        print(f"学号：{student[0]}, 姓名：{student[1]}, 性别：{student[2]}, 地址：{student[3]}, 电话：{student[4]}, 邮箱：{student[5]}")
    
    print("\n")
    
    # 2. 用list存储学生信息
    list_students = create_list_student_info()
    print("=== 列表存储的学生信息 ===")
    for student in list_students:
        print(f"学号：{student[0]}, 姓名：{student[1]}, 性别：{student[2]}, 地址：{student[3]}, 电话：{student[4]}, 邮箱：{student[5]}")
    
    print("\n")
    
    # 3. 用dict存储学生信息
    dict_students = create_dict_student_info()
    print("=== 字典存储的学生信息 ===")
    for student_id, info in dict_students.items():
        print(f"学号：{student_id}, 姓名：{info['name']}, 性别：{info['gender']}, 地址：{info['address']}, 电话：{info['phone']}, 邮箱：{info['email']}")

if __name__ == "__main__":
    main() 