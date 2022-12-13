#编写业务方法
import orm
import random
import main
import hashlib

#1) 导入库
import PySimpleGUI as sg
#2) 定义布局，确定行数


#5) 关闭窗口

#查看商品列表
def getAllProducts():
	sql="SELECT * FROM products;"
	data=orm.getData(sql)
	tit=['序号','编号','名称','单价','折扣']
	layout = [[sg.Table(data,headings=tit)
],
			  [sg.Button('返回首页',key='-return-',size=(40,3))]]
	# 3) 创建窗口
	window_gp = sg.Window('查看商品信息',layout)
	# 4) 事件循环
	while True:
		event, values = window_gp.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
		# print(event, values)
		if event == None:  # 窗口关闭事件
			break
		if event=='-return-':
			window_gp.close()
			main.main()


#根据编号查询商品
def getProduct():
	layout=[[sg.Input('请输入商品编号',font=('宋体',20),size=(20,4),key='-input-')],
			[sg.B('确认',key='-ok-',size=(15,2)),sg.B('取消',key='-cancel-',size=(15,2))]
			,[sg.B('返回首页',key='-return-',size=(32,2))]]
	window_sp = sg.Window('根据编号查询商品', layout, resizable=True)
	while True:
		event, values = window_sp.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
		# print(event, values['-input-'])
		if event == None:  # 窗口关闭事件
			break
		if event=='-cancel-':
			continue
		if event=='-return-':
			window_sp.close()
			main.main()
		if event=='-ok-':

			num = str(values['-input-'])
			print(num)
			sql = "SELECT * FROM products WHERE num=" + num + ";"
			data = orm.getData(sql)
			try:
				sg.popup('商品名称：',data[0][2],'单价：',data[0][3],'折扣：',data[0][4])

			except:
				sg.popup('商品不存在')


#添加商品
def addProduct():
	layout = [[sg.Input('请输入商品名称', font=('宋体', 20), size=(20, 4), key='-name-')],
			  [sg.Input('请输入商品价格', font=('宋体', 20), size=(20, 4), key='-price-')],
			  [sg.B('确认', key='-ok-', size=(15, 2)), sg.B('取消', key='-cancel-', size=(15, 2))]
		, [sg.B('返回首页', key='-return-', size=(32, 2))]]
	window_ap = sg.Window('添加商品', layout, resizable=True)
	while True:
		event, values = window_ap.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
		name=values['-name-']
		price=values['-price-']
		num=str(random.randint(1000,9999))
		if event == None:  # 窗口关闭事件
			break
		if event == '-cancel-':
			continue
		if event == '-return-':
			window_ap.close()
			main.main()
		if event == '-ok-':
			sql = "INSERT INTO products(num,name,price,discount) VALUES(" + num + ",'" + name + "'," + price + ",1);"
			orm.writeData(sql)
			sg.popup('产品添加成功！')

#根据编号删除商品
def delProduct():
	layout = [[sg.Input('请输入商品编号', font=('宋体', 20), size=(20, 4), key='-id-')],
			  [sg.B('确认', key='-ok-', size=(15, 2)), sg.B('取消', key='-cancel-', size=(15, 2))]
		, [sg.B('返回首页', key='-return-', size=(32, 2))]]
	window_dp = sg.Window('根据编号删除商品', layout, resizable=True)
	while True:
		event, values = window_dp.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
		num = values['-id-']
		if event == None:  # 窗口关闭事件
			break
		if event == '-cancel-':
			continue
		if event == '-return-':
			window_dp.close()
			main.main()
		if event == '-ok-':
			sql = "DELETE FROM products WHERE num=" + num + ";"
			r = orm.writeData(sql)
			if r==0:
				sg.popup('删除失败')
			else:
				sg.popup('产品',num,'删除成功！')

#商品打折（修改折扣）
def setDiscount():
	layout = [[sg.Input('请输入商品编号', font=('宋体', 20), size=(20, 4), key='-num-')],
			  [sg.Input('请输入折扣0.1-1', font=('宋体', 20), size=(20, 4), key='-discount-')],
			  [sg.B('确认', key='-ok-', size=(15, 2)), sg.B('取消', key='-cancel-', size=(15, 2))]
		, [sg.B('返回首页', key='-return-', size=(32, 2))]]
	window_sd = sg.Window('商品打折', layout, resizable=True)
	while True:
		event, values = window_sd.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
		if event == None:  # 窗口关闭事件
			break
		if event == '-cancel-':
			continue
		if event == '-return-':
			window_sd.close()
			main.main()
		if event == '-ok-':
			num = values['-num-']
			discount = float(values['-discount-'])
			print(num,discount)
			if 0.1 <= discount <= 1:
				sql = "UPDATE products SET discount=" + str(discount) + " WHERE num=" + num + ";"
				r = orm.writeData(sql)
				if r == 0:
					sg.popup('设置失败！')
				else:
					sg.popup('商品', num, '折扣设置成功！')
			else:
				sg.popup('折扣输入错误！')





# 查看所有订单；
def getAllOrders():
	sql = "SELECT * FROM orders;"
	data = orm.getData(sql)
	tit = ['序号', '编号', '数量', '金额']
	layout = [[sg.Table(data, headings=tit)
			   ],
			  [sg.Button('返回首页', key='-return-', size=(40, 3))]]
	# 3) 创建窗口
	window_ad = sg.Window('查看所有订单', layout)
	# 4) 事件循环
	while True:
		event, values = window_ad.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
		# print(event, values)
		if event == None:  # 窗口关闭事件
			break
		if event == '-return-':
			window_ad.close()
			main.main()

# 删除订单；（通过订单号删除）
def delOrder():
	layout = [[sg.Input('请输入订单编号', font=('宋体', 20), size=(20, 4), key='-id-')],
			  [sg.B('确认', key='-ok-', size=(15, 2)), sg.B('取消', key='-cancel-', size=(15, 2))]
		, [sg.B('返回首页', key='-return-', size=(32, 2))]]
	window_dd = sg.Window('根据编号删除订单', layout, resizable=True)
	while True:
		event, values = window_dd.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
		num = values['-id-']
		if event == None:  # 窗口关闭事件
			break
		if event == '-cancel-':
			continue
		if event == '-return-':
			window_dd.close()
			main.main()
		if event == '-ok-':
			sql = "DELETE FROM orders WHERE num=" + num + ";"
			r = orm.writeData(sql)
			if r == 0:
				sg.popup('删除失败')
			else:
				sg.popup('产品', num, '删除成功！')


# 订单统计(总销量，销售额)；
def accordOrder():
	sql="SELECT * FROM orders;"
	data=orm.getData(sql)
	totalCount=0
	totalAmount=0
	for order in data:
		totalCount+=order[2]
		totalAmount+=order[3]
		text='总销售量:{}件！销售额{}元！'.format(totalCount,totalAmount)
	layout = [[sg.T(text, font=('宋体', 20), size=(20, 4), key='-text-')],
		 [sg.B('返回首页', key='-return-', size=(32, 2))]]
	window_tj = sg.Window('订单统计', layout, resizable=True)
	while True:
		event, values = window_tj.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
		if event == None:  # 窗口关闭事件
			break
		if event == '-return-':
			window_tj.close()
			main.main()


#商品结算
def settle():
	orderCount=0
	orderAmount=0
	msg=0 #保存订单是否有效
	layout = [[sg.Input('请输入商品编号', font=('宋体', 20), size=(20, 4), key='-id-')],
			  [sg.Input('请输入商品数量', font=('宋体', 20), size=(20, 4), key='-sl-')],
			  [sg.B('确认', key='-ok-', size=(15, 2)), sg.B('结算', key='-settle-', size=(15, 2))]
		, [sg.B('返回首页', key='-return-', size=(32, 2))]]
	window_st = sg.Window('商品结算', layout, resizable=True)
	while True:
		event, values = window_st.read(timeout=100)  # 窗口的读取，有两个返回值(1.事件  2.值)
		if event == None:  # 窗口关闭事件
			break
		if event == '-return-':
			window_st.close()
			main.main()
		if event == '-ok-' and values['-id-']!='请输入商品编号'and values['-sl-']!='请输入商品数量':
			num = str(values['-id-'])
			# print(type(values['-sl-']))
			sl=float(values['-sl-'])
			sql = "SELECT * FROM products WHERE num=" + num + ";"
			data = orm.getData(sql)
			# print(data)
			# print(data[0][3],data[0][4])
			if len(data) != 0:
				msg = 1
				price = data[0][3]
				discount = data[0][4]
				amount = price * sl * discount
				orderCount += sl
				orderAmount += amount
				sg.popup('当前添加{}件！金额{}元！'.format(sl,amount))
			else:
				sg.popup('没有该商品！')
		if event == '-settle-':
			sg.popup('您购买的总数量：{}件，总金额：{}元！'.format(orderCount, orderAmount))
			if msg == 1:
				oid = str(random.randint(1000, 9999))
				sql = "INSERT INTO orders(num,count,amount) VALUES(" + oid + "," + str(orderCount) + "," + str(
					orderAmount) + "); "
				orm.writeData(sql)
				sg.popup('订单添加成功！')

#登录
def login():
	layout = [[sg.Input('请输入用户名', font=('宋体', 20), size=(20, 4), key='-uname-')],
			  [sg.Input('请输入密码', font=('宋体', 20), size=(20, 4), key='-key-')],
			  [sg.B('登录', key='-login-', size=(10, 2)), sg.B('取消', key='-cancel-', size=(10, 2)),sg.B('注册', key='-reg-', size=(10, 2))]
		]
	window_lg = sg.Window('登录窗口', layout, resizable=True)
	while True:
		event, values = window_lg.read(timeout=100)  # 窗口的读取，有两个返回值(1.事件  2.值)
		if event is None:  # 窗口关闭事件
			break
		if event=='-login-':
			uname=values['-uname-']
			upwd=values['-key-']
			sql="SELECT * FROM users WHERE username='"+uname+"' and password='"+upwd+"'"
			data=orm.getData(sql)
			print(data)
			if len(data)==0:
				sg.popup("登录失败！")
			else:
				sg.popup("登录成功！")
				window_lg.close()
				main.main()
		if event=='-cancel-':
			pass
		if event=='-reg-':
			window_lg.close()
			reg()


# 注册（在数据库中增加用户）
def reg():
	while True:
		layout = [[sg.Input('请输入用户名', font=('宋体', 20), size=(20, 4), key='-uname-')],
				  [sg.Input('请输入密码', font=('宋体', 20), size=(20, 4), key='-key-')],
				  [sg.Input('请输入昵称', font=('宋体', 20), size=(20, 4), key='-nknm-')],
				  [sg.B('确认', key='-ok-', size=(10, 2)), sg.B('取消', key='-cancel-', size=(10, 2))]
				  ]
		window_rg = sg.Window('注册新账户', layout, resizable=True)
		while True:
			event, values = window_rg.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
			if event=='-ok-':
				newuser=values['-uname-']
				newpass = values['-key-']
				newname = values['-nknm-']
				sql = "SELECT * FROM users WHERE username='" + newuser + "';"
				data = orm.getData(sql)
				if len(data) != 0:
					sg.popup("此用户已注册")
				else:
					sql = "INSERT INTO users(id,username,password,nickname) VALUES(null,'" + str(newuser) + "','" + str(
						newpass) + "','" + str(newname) + "'); "
					# print(sql)
					orm.writeData(sql)
					window_rg.close()
					sg.popup("新用户添加成功！")
					login()
			if event=='-cancel-':
				break

