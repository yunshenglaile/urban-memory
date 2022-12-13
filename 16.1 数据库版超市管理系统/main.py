#调用
import market
import PySimpleGUI as sg

def main():

	lst=['1.查看商品列表','2.根据编号查询商品','3.添加商品','4.根据编号删除商品','5.商品打折','6.查看所有订单'
		,'7.删除订单','8.订单统计','9.商品结算','10.退出']
	layout = [
			[sg.Text('超市管理系统',size=(20,2),justification='center',font=('宋体',18),text_color='red')]
			,[sg.Button(lst[0], size=(30,2),key='-B1-')]
			,[sg.Button(lst[1], size=(30,2),key='-B2-')]
			, [sg.Button(lst[2], size=(30, 2),key='-B3-')]
			, [sg.Button(lst[3], size=(30, 2),key='-B4-')]
			, [sg.Button(lst[4], size=(30, 2),key='-B5-')]
			, [sg.Button(lst[5], size=(30, 2),key='-B6-')]
			, [sg.Button(lst[6], size=(30, 2),key='-B7-')]
			, [sg.Button(lst[7], size=(30, 2),key='-B8-')]
			, [sg.Button(lst[8], size=(30, 2),key='-B9-')]
			, [sg.Button(lst[9], size=(30, 2), key='-B10-')]
				]
	window_main=sg.Window('超市管理系统',layout)
	while True:
		event, values = window_main.read()
		# print(event, values)
		if event == None:
			break
		if event == '-B1-':
			window_main.close()
			market.getAllProducts()
		if event == '-B2-':
			window_main.close()
			market.getProduct()
		if event == '-B3-':
			window_main.close()
			market.addProduct()
		if event == '-B4-':
			window_main.close()
			market.delProduct()
		if event == '-B5-':
			window_main.close()
			market.setDiscount()
		if event == '-B6-':
			window_main.close()
			market.getAllOrders()
		if event == '-B7-':
			window_main.close()
			market.delOrder()
		if event == '-B8-':
			window_main.close()
			market.accordOrder()
		if event == '-B9-':
			window_main.close()
			market.settle()
		if event == '-B10-':
			window_main.close()
			break
		else:
			pass



if __name__ == '__main__':
	market.login()
	# market.reg()
	# main()