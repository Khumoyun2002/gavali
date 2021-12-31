import telebot, openpyxl, time, os
import cv2
import generate, scan, start, baza, tochka
from telebot import types
from PIL import Image, ImageDraw
bot = telebot.TeleBot('1422462057:AAE4ls6Bppi9OmF-AvY9Ic3UOidGScvgZB8')



while  True:
	try:
		nomer = ""


		regru = types.ReplyKeyboardMarkup(resize_keyboard=True)
		reg1 = types.KeyboardButton(text = "Пройти регистрацию 📝")
		regru.add(reg1)

		reguzz = types.ReplyKeyboardMarkup(resize_keyboard=True)
		reguz1 = types.KeyboardButton(text = "Руйхатдан утиш 📝")
		reguzz.add(reguz1)

		#АДМИН ПАНЕЛЬ



		#ЯЗЫК АДМИН

		admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
		admin1 = types.KeyboardButton(text = "Статистика 📈")
		admin3 = types.KeyboardButton(text = "Активные Cashback 💸")
		admin4 = types.KeyboardButton(text = "Топ клиенты 🔝")
		admin5 = types.KeyboardButton(text = "Список клиентов  📜")
		admin6 = types.KeyboardButton(text = "Все операции  📊")
		admin.add(admin1, admin3, admin4 , admin5, admin6)

		operatsi = types.InlineKeyboardMarkup(row_width = 1)
		operatsi1 = types.InlineKeyboardButton( text = "Сегодня", callback_data='bugun')
		operatsi2 = types.InlineKeyboardButton( text = "Эта неделя", callback_data='hafta')
		operatsi3 = types.InlineKeyboardButton( text = "Этот месяц", callback_data='oy')
		operatsi4 = types.InlineKeyboardButton( text = "За весь период", callback_data='hammasi')
		operatsi.add(operatsi1, operatsi2, operatsi3, operatsi4)


		sttt = types.InlineKeyboardMarkup(row_width =2)
		st1 = types.InlineKeyboardButton( text = "Кукча", callback_data='kukcha')
		st2 = types.InlineKeyboardButton( text = "Ц1", callback_data='s1')
		st3 = types.InlineKeyboardButton( text = "Общая статистика", callback_data='obshiysi')
		sttt.add(st1,st2,st3)


		fillial = ""
		########################################

		#Кассир Панель

		# 1048549452 = Исроилова Рано
		# 112793473 = Маматкулова Дильноза
		# 342770270 = Исмоилов Ислом
		# 854715014 = Султанова Азиза
		# 1142977382 = Дилором
		# 1883755 = Ирода
		# 448696831 = Нозима
		# 1341225206 = Муслим
		# 411938418 = Шохиста


		customer = [ "4296573641", "375749475", "1339452077",  "1048549452", "112793473",  "342770270", "854715014", "1142977382", "1883755", "448696831", "1341225206", "411938418"]


		glav = ["429657364", "419572521", "2407095", "898066732"]


		#ЯЗЫК КАССИР
		tlcassir = types.InlineKeyboardMarkup()
		tl5 = types.InlineKeyboardButton( text = "Русский 🇷🇺", callback_data='rucassir')
		tl6 = types.InlineKeyboardButton(text = "Узбек тили 🇺🇿", callback_data='uzcassir')
		tlcassir.add(tl5, tl6)

		kassir = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
		kassirr1 = types.KeyboardButton(text = "Cashback 🎁")
		kassirr2 = types.KeyboardButton(text = "Оплата 💵")
		kassirr3 = types.KeyboardButton(text = "Статистика 📊")
		kassir.add(kassirr1, kassirr2, kassirr3)

		var = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
		var1 = types.KeyboardButton(text = "По QR код или Gavali ID!")
		var2 = types.KeyboardButton(text = "По номеру телефона !")
		var3 = types.KeyboardButton(text = "Главное меню !")
		var.add(var1, var2, var3)

		period = types.InlineKeyboardMarkup(row_width = 1)
		per1 = types.InlineKeyboardButton(text = "Статистика за сегодня !", callback_data='Статистика на сегодня !')
		per2 = types.InlineKeyboardButton(text = "Статистика за эту неделю !", callback_data='Статистика на эту неделю !' )
		per3 = types.InlineKeyboardButton(text = "Статистика за этот месяц !", callback_data='Статистика на этот месяц !')
		period.add(per1, per2, per3, )



		########################################


		#Клиент Панель

		kassir1 = ""
		kassir2 = ""
		kassir3 = ""
		kassir4 = ""
		kassir5 = ""
		kassir6 = ""

		######## RUS TILIDA
		kontakt = types.InlineKeyboardMarkup(row_width = 1)
		kontakt1 = types.InlineKeyboardButton( text = "Мы в Instagram 🔹 ", url = 'https://www.instagram.com/gavali_uzbekistan')
		kontakt2 = types.InlineKeyboardButton(text = "Мы в Facebook 🔹 ", url = 'https://www.facebook.com/gavali.uzbekistan/' )
		kontakt3 = types.InlineKeyboardButton(text = "Наш сайт 🔹 ", url = 'https://www.gavali.uz')
		kontakt.add(kontakt1, kontakt2, kontakt3)

		tl = types.InlineKeyboardMarkup()
		tl3 = types.InlineKeyboardButton( text = "Русский 🇷🇺", callback_data='ru')
		tl4 = types.InlineKeyboardButton(text = "Узбек тили 🇺🇿", callback_data='uz')
		tl.add(tl3, tl4)

		tel = types.ReplyKeyboardMarkup(resize_keyboard=True)
		tel1 = types.KeyboardButton(text = "Отправить номер телефона", request_contact=True)
		tel.add(tel1)


		otm = types.ReplyKeyboardMarkup(resize_keyboard=True)
		otm1 = types.KeyboardButton(text = "Отменить")
		otm.add(otm1)


		menyu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
		menyu1 = types.KeyboardButton(text = "Мои данные 🔐")
		menyu2 = types.KeyboardButton(text = "Мой баланс 💵")
		menyu4 = types.KeyboardButton(text = "Контакты 📞")
		menyu5 = types.KeyboardButton(text = "Адреса магазинов 📍")
		menyu.add(menyu1, menyu2, menyu5, menyu4)


		adres = types.InlineKeyboardMarkup()
		adres1 = types.InlineKeyboardButton( text = "Кукча 🟢", callback_data='adres1')
		adres2 = types.InlineKeyboardButton(text = "Ц1 🔵", callback_data='adres2')
		adres.add(adres1, adres2)

		################ UZBEK TILIDA

		kontaktuz = types.InlineKeyboardMarkup(row_width = 1)
		kontaktuz1 = types.InlineKeyboardButton( text = "Instagram саҳифамиз 🔹 ", url = 'https://www.instagram.com/gavali_uzbekistan')
		kontaktuz2 = types.InlineKeyboardButton(text = "Facebook саҳифамиз 🔹 ", url = 'https://www.facebook.com/gavali.uzbekistan/' )
		kontaktuz3 = types.InlineKeyboardButton(text = "Бизнинг сайт 🔹 ", url = 'https://www.gavali.uz')
		kontaktuz.add(kontaktuz1, kontaktuz2, kontaktuz3)


		teluz = types.ReplyKeyboardMarkup(resize_keyboard=True)
		teluz1 = types.KeyboardButton(text = "Телефон ракамингизни юбориш !", request_contact=True)
		teluz.add(teluz1)


		otmuz = types.ReplyKeyboardMarkup(resize_keyboard=True)
		otmuz1 = types.KeyboardButton(text = "Бекор килиш !")
		otmuz.add(otmuz1)


		menyuuz = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
		menyuuz1 = types.KeyboardButton(text = "Менинг маълумотларим 🔐")
		menyuuz2 = types.KeyboardButton(text = "Менинг балансим 💵")
		menyuuz4 = types.KeyboardButton(text = "Контактлар 📞")
		menyuuz5 = types.KeyboardButton(text = "Магазинлар адреси 📍")
		menyuuz.add(menyuuz1, menyuuz2, menyuuz5, menyuuz4)


		adresuz = types.InlineKeyboardMarkup()
		adresuz1 = types.InlineKeyboardButton( text = "Кукча 🟢", callback_data='adres1uz')
		adresuz2 = types.InlineKeyboardButton(text = "Ц1 🔵", callback_data='adres2uz')
		adresuz.add(adresuz1, adresuz2)










		reg = []
		reguz = []

		########################################
		@bot.message_handler(commands=['start'])
		def boshi(message):
			global customer, glav
			profilid= message.chat.id
			start.startt(chatid = str(profilid))
			if str(message.chat.id) in glav:
				bot.send_message(message.chat.id, "Здравстуйте " + str(message.from_user.first_name)+" ✅ ", reply_markup = admin)

			if str(message.chat.id) in customer:
			    bot.send_message(message.chat.id, "Здравстуйте " + str(message.from_user.first_name)+" ✅ ", reply_markup = kassir)
			else:
				if str(message.chat.id) in glav:
					pass
				else:

					bot.send_message(message.chat.id, "Выберите язык : \nТилни танланг : ", reply_markup = tl)

		##############################
		@bot.callback_query_handler(func = lambda call: True)
		def inline(call):
			global reg, reguz,fillial
			if call.data == "ru":
				cid = call.message.chat.id

				#print(cid)
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы выбрали Русский язык 🇷🇺", reply_markup=None)
				test = baza.idtekshiruv(chatid = str(cid))
				#print(test)
				if test == "Янги":
					bot.send_message(call.message.chat.id,"Для получения Cashback вам следует пройти регистрацию )")

					bot.send_message(call.message.chat.id, "Регистрация : Для отправки номера нажмите на появивщуюся кнопку ! ", reply_markup = tel)
					reg.append(cid)
					try:
						reguz.remove(str(call.message.chat.id))
						try:
							reguz.remove(str(call.message.chat.id))
						except Exception:
							pass
					except Exception:
						pass
				else:
					baza.changelang(x = str(cid), y = "ru")
					bot.send_message(call.message.chat.id,"Добро пожаловать на накопительную система бутика элитных сладостей Gavali !", reply_markup = menyu)



			if call.data ==  "adres1":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отпралена геолокация филиала Gavali-Кукча 📍", reply_markup=None)
				bot.send_location(call.message.chat.id,  latitude = 41.322453, longitude = 69.207956)
				bot.send_message(call.message.chat.id, "Шайхантахурский район,ул. Кукча дарвоза, 346\nОриентир: Мечеть Кукча ")


			if call.data ==  "adres2":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отпралена геолокация филиала Gavali-Ц1 📍", reply_markup=None)
				bot.send_location(call.message.chat.id,  latitude = 41.305591, longitude = 69.283001)
				bot.send_message(call.message.chat.id, "Мирабадский район,ул. Шахрисабзская 5А.\nОриентир: Международный Вестминстерский Университет, Узбекнефтегаз")

			##################### UZBEKCHA
			if call.data == "uz":
				cid = call.message.chat.id
				print(cid)
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Сиз узбек тилини танладингиз 🇺🇿 ", reply_markup=None)
				test = baza.idtekshiruv(chatid = str(cid))
				print(test)
				if test == "Янги":
					bot.send_message(call.message.chat.id,"Cashback олиш учун руйхатдан утинг )")

					bot.send_message(call.message.chat.id, "Руйхатдан утиш : Телефон ракамни юбориш учун пайдо булган тугмагачани босинг ! ", reply_markup = teluz)
					reg.append(cid)
					if str(cid) in reguz:
						pass
					else:
						reguz.append(str(cid))
				else:
					baza.changelang(x = str(cid), y = "uz")
					bot.send_message(call.message.chat.id,"Gavali ширинликлар бутикининг виртуал Cashback тизимига Хуш Келибсиз !", reply_markup = menyuuz)

			if call.data ==  "adres1uz":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Gavali-Кукча филиалининг геолокацияси юборилди 📍", reply_markup=None)
				bot.send_location(call.message.chat.id,  latitude = 41.322453, longitude = 69.207956)
				bot.send_message(call.message.chat.id, "Шайхонтахур тумани, Кукча дарвоза 346\Мўлжал: Кукча Масжиди ")


			if call.data ==  "adres2uz":
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ц1 филиалининг геолокацияси юборилди 📍", reply_markup=None)
				bot.send_location(call.message.chat.id,  latitude = 41.305591, longitude = 69.283001)
				bot.send_message(call.message.chat.id, "Миробод тумани, Шахрисабз кучаси 5А.\nОриентир: Международный Вестминстерский Университет, Узбекнефтегаз")


		################ ADMINDIKI
			if call.data == "bugun":
				if fillial == "Кукча":
					popolneno, potracheno = baza.statadmin(x = "1", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика филиала Кукча :\nСегодня зачислено : "+str(popolneno) +" Gavali монеток\n\nСегодня снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
				if fillial =="Ц1":
					popolneno, potracheno = baza.statadmin(x = "1", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика филиала Ц1 :\nСегодня зачислено : "+str(popolneno) +" Gavali монеток\n\nСегодня снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
				if fillial =="Обший":
					popolneno, potracheno = baza.statadmin(x = "1", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика всех филиалов :\nСегодня зачислено : "+str(popolneno) +" Gavali монеток\n\nСегодня снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)

			if call.data == "hafta":
				print("norm")
				if fillial == "Кукча":
					popolneno, potracheno = baza.statadmin(x = "7", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика филиала Кукча :\nНа этой недели зачислено : "+str(popolneno) +" Gavali монеток\n\nНа этой недели снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
				if fillial =="Ц1":
					popolneno, potracheno = baza.statadmin(x = "7", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика филиала Ц1 :\nНа этой недели зачислено : "+str(popolneno) +" Gavali монеток\n\nНа этой недели снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
				if fillial =="Обший":
					popolneno, potracheno = baza.statadmin(x = "7", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика всех филиалов :\nНа этой недели зачислено : "+str(popolneno) +" Gavali монеток\n\nНа этой недели снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
			if call.data == "oy":
				if fillial == "Кукча":
					popolneno, potracheno = baza.statadmin(x = "oy", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика филиала Кукча :\nНа этом месяце зачислено : "+str(popolneno) +" Gavali монеток\n\nНа этом месяце снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
				if fillial =="Ц1":
					popolneno, potracheno = baza.statadmin(x = "oy", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика филиала Ц1 :\nНа этом месяце зачислено : "+str(popolneno) +" Gavali монеток\n\nНа этом месяце снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
				if fillial =="Обший":
					popolneno, potracheno = baza.statadmin(x = "oy", y = fillial)
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика всех филиалов :\nНа этом месяце зачислено : "+str(popolneno) +" Gavali монеток\n\nНа этом месяце снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
			if call.data == "hammasi":
				if fillial == "Кукча":
					popolneno, potracheno = baza.statadmin(x = "hammasi", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика филиала Кукча :\nЗа весь период зачислено : "+str(popolneno) +" Gavali монеток\n\nЗа весь период  снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
				if fillial =="Ц1":
					popolneno, potracheno = baza.statadmin(x = "hammasi", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика филиала Ц1 :\nЗа весь период зачислено : "+str(popolneno) +" Gavali монеток\n\nЗа весь период снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)
				if fillial =="Обший":
					popolneno, potracheno = baza.statadmin(x = "hammasi", y = fillial)
					popolneno = tochka.tochka(x = str(popolneno))
					potracheno = tochka.tochka(x = str(potracheno))
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Статистика всех филиалов :\nЗа весь период зачислено : "+str(popolneno) +" Gavali монеток\n\nЗа весь период снято : " + str(potracheno) +" Gavali монеток", reply_markup=None)

			if call.data == "kukcha":
				fillial = "Кукча"
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите нужный период !", reply_markup=operatsi )
			if call.data == "s1":
				fillial = "Ц1"
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите нужный период !", reply_markup=operatsi )
			if call.data == "obshiysi":
				fillial = "Обший"
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите нужный период !", reply_markup=operatsi )


		####
			if call.data == "Статистика на сегодня !":
				popolnen, potrachen = baza.stat(x = "1", y = str(call.message.chat.id))
				popolnen = tochka.tochka(x = str(popolnen))
				potrachen = tochka.tochka(x = str(potrachen))
				a = "Сегодня вы зачислили : "+str(popolnen)+" Gavali монеток\n_______________________\nСняли : "+str(potrachen)+" Gavali монеток"
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = a, reply_markup = None)

			elif call.data == "Статистика на эту неделю !":
				popolnen, potrachen = baza.stat(x = "7", y = str(call.message.chat.id))
				popolnen = tochka.tochka(x = str(popolnen))
				potrachen = tochka.tochka(x = str(potrachen))
				a = "На этой недели вы зачислили : "+str(popolnen)+" Gavali монеток\n_______________________\nСняли : "+str(potrachen)+" Gavali монеток"
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = a, reply_markup = None)

			elif call.data == "Статистика на этот месяц !":
				popolnen, potrachen = baza.stat(x = "oy", y = str(call.message.chat.id))
				popolnen = tochka.tochka(x = str(popolnen))
				potrachen = tochka.tochka(x = str(potrachen))
				a = "На этом месяце вы добавили : "+str(popolnen)+" Gavali монеток\n_______________________\nПотратили : "+str(potrachen)+" Gavali монеток"
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = a, reply_markup = None)

			else:
				wb = openpyxl.reader.excel.load_workbook(filename="baza3.xlsx")
				wb.active = 0
				sheet = wb.active

				if "нет" in call.data :
					q = 1
					data = call.data[0]+call.data[1]+call.data[2]+call.data[3]+call.data[4]+call.data[5]+call.data[6]+call.data[7]
					print(data)
					while q < 20000:
						if str(sheet["G"+str(q)].value) == data and str(sheet["F"+str(q)].value) == "Нет":
							til, ism = baza.findlang(x = str(call.message.chat.id))
							if til == "Русский язык":
								sheet["F"+str(q)].value = ("Отклонено")
								ismklienta =  sheet["A"+str(q)].value
								zz = str(sheet["E"+str(q)].value)
								#print("yaxsh21321i")
								bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = "Платёж отклонён !", reply_markup = None)
								bot.send_message(zz, "Оплата клиента "+ ism +" была отклонена !", reply_markup = kassir)
								wb.save("baza3.xlsx")
							if til == "Узбек тили":
								sheet["F"+str(q)].value = ("Отклонено")
								ismklienta =  sheet["A"+str(q)].value
								zz = str(sheet["E"+str(q)].value)
								#print("yaxsh21321i")
								bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = "Тулов рад этилди !", reply_markup = None)
								bot.send_message(zz, "Оплата клиента "+ ism +" была отклонена !", reply_markup = kassir)
								wb.save("baza3.xlsx")
							break
						q = q +1
				else:
					i = 1
					while i < 20000:
						if str(sheet["G"+str(i)].value) == call.data and str(sheet["F"+str(i)].value) == "Нет":

							zz = str(sheet["E"+str(i)].value)
							yy = str(sheet["D"+str(i)].value)
							xx = str(sheet["C"+str(i)].value)
							#print("yy")
							til, ism2 = baza.findlang(x = str(call.message.chat.id))
							if til == "Русский язык":
								klient,moneta, balans,ism = baza.oplata(x = str(xx), y = str(yy), z = str(zz))
								yy = tochka.tochka(x = str(yy))
								bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text = "Оплачено "+ yy +" Gavali монеток", reply_markup = None)

								bot.send_message(zz, "Оплата клиента  "+ ism +" была подтверждена !\nСнято "+ yy +" Gavali монеток", reply_markup = kassir)
								#print("yaxshii")
								sheet["F"+str(i)].value = ("Да")
							if til == "Узбек тили":
								klient,moneta, balans,ism = baza.oplata(x = str(xx), y = str(yy), z = str(zz))
								yy = tochka.tochka(x = str(yy))
								bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text =  yy +" Gavali тангачалари туланди !", reply_markup = None)
								bot.send_message(zz, "Оплата клиента  "+ ism +" была подтверждена !\nСнято "+ yy +" Gavali монеток", reply_markup = kassir)
								#print("yaxshii")
								sheet["F"+str(i)].value = ("Да")
							wb.save('baza3.xlsx')
							break
						i = i +1


		######################################    REGISTRATSIYA
		@bot.message_handler(content_types=['contact'])
		def read_contact_phone(message):
		    phone_usm = message.contact.phone_number
		    print(phone_usm)
		    global nomer, reg, reguz



		    if str(message.chat.id) in reguz:
		    	if message.chat.id in reg:
				    if "+" in str(phone_usm):
				    	nomer = str(phone_usm)
				    	baza.qushish(x = str(nomer))
				    	bot.send_message(message.chat.id, "Номер тасдикланди !", reply_markup = None)
				    	bot.send_message(message.chat.id, "Фамилия исмингизни киритинг !", reply_markup = otmuz)
				    	bot.register_next_step_handler(message, FIO )

				    else :
				    	nomer = "+" + str(phone_usm)
				    	baza.qushish(x = str(nomer))
				    	bot.send_message(message.chat.id, "Номер тасдикланди !", reply_markup = None)
				    	bot.send_message(message.chat.id, "Фамилия исмингизни киритинг !", reply_markup = otmuz)
				    	bot.register_next_step_handler(message, FIO )

				    reg.remove(message.chat.id)



		    else:
		    	if message.chat.id in reg :
				    if "+" in str(phone_usm):
				    	nomer = str(phone_usm)
				    	baza.qushish(x = str(nomer))
				    	bot.send_message(message.chat.id, "Номер добавлен !", reply_markup = None)
				    	bot.send_message(message.chat.id, "Напишите Ф.И.О", reply_markup = otm)
				    	bot.register_next_step_handler(message, FIO )
				    else :
				    	nomer = "+" + str(phone_usm)
				    	baza.qushish(x = str(nomer))
				    	bot.send_message(message.chat.id, "Номер добавлен !", reply_markup = None)
				    	bot.send_message(message.chat.id, "Напишите Ф.И.О", reply_markup = otm)
				    	bot.register_next_step_handler(message, FIO )
				    reg.remove(message.chat.id)



		############################################



		@bot.message_handler(content_types=['text'])
		def obshiy(message):
			global customer, reg, reguz, glav
			cid = message.chat.id

			test = baza.idtekshiruv(chatid = str(cid))


			if str(message.chat.id) in glav:
				if message.text == "Статистика 📈":
					bot.send_message(message.chat.id, "Выберите нужный филиал !", reply_markup = sttt )


				if message.text == "Активные Cashback 💸":
					wb = openpyxl.reader.excel.load_workbook(filename="baza.xlsx")
					wb.active = 0
					sheet = wb.active
					vsego = 0
					chislo = 0
					i = 2
					while 1 < 20000:
						if str(sheet['E'+str(i)].value) != "None":
							vsego = vsego + sheet['E'+str(i)].value
							chislo = chislo+1

						else:
							break
						i = i+1
					vsego = tochka.tochka(x = str(vsego))
					chislo = tochka.tochka( x= str(chislo))
					bot.send_message(message.chat.id, "Сейчас активно : " + str(chislo) + " пользователей\nСейчас активно : " +str(vsego)+" Gavali монеток")
				if message.text == "Топ клиенты 🔝":
					bot.send_message(message.chat.id, "Сабр клин энди ишлеман !")

				if message.text == "Список клиентов  📜":
					a = open('baza.xlsx', 'rb')
					bot.send_document(message.chat.id, a)

				if message.text == "Все операции  📊":
					a = open('baza2.xlsx', 'rb')
					bot.send_document(message.chat.id, a)

				if message.text != "Статистика 📈" and message.text != "Активные Cashback 💸" and message.text != "Топ клиенты 🔝" and message.text !=  "Список клиентов  📜" and message.text != "Все операции  📊":
					bot.send_message(message.chat.id, "Выберите одну из действий !", reply_markup = admin)



		#####
			if str(message.chat.id) in customer:
				if message.text == "Cashback 🎁":
					bot.send_message(message.chat.id, "Выберите метод добавление Cashback !", reply_markup = var)
					bot.register_next_step_handler(message, VAR )


				if message.text == "Оплата 💵":
					bot.send_message(message.chat.id, "Выберите метод оплаты !", reply_markup = var)
					bot.register_next_step_handler(message, VAR2 )
				if message.text == "Статистика 📊":
					bot.send_message(message.chat.id, "Выберите период :", reply_markup = period)


				if message.text != 	"Cashback 🎁" and message.text != "Оплата 💵" and  message.text != "Статистика 📊":
				    bot.send_message(message.chat.id, "Выберите действие !", reply_markup = kassir)


		############################################  KKKLLLIIIEEENNNTTT


			if test == "Янги" :
				if message.text == "Пройти регистрацию 📝":
					bot.send_message(message.chat.id, "Регистрация : Для отправки номера нажмите на появившую кнопку ! ", reply_markup = tel)
					reg.append(cid)
				elif message.text == "Руйхатдан утиш 📝":
					bot.send_message(message.chat.id, "Руйхатдан утиш : Телефон ракамни юбориш учун пайдо булган тугмага босинг !", reply_markup = teluz)
					if str(cid) in reguz:
						pass
					else:
						reguz.append(str(cid))
					reg.append(cid)
				else:
				    if str(message.chat.id) in customer or str(message.chat.id) in glav:
				        pass
				    else:
				    	bot.send_message(message.chat.id, "Выберите язык : \nТилни танланг : ", reply_markup = tl)




			else:
				################### RUSKIY
				til, ism = baza.findlang(x = str(message.chat.id))
				if til =="Русский язык":
					if str(message.chat.id) in customer:
						pass
					if str(message.chat.id) in glav:
						pass
					else:
						if message.text == "Адреса магазинов 📍":
							bot.send_message(message.chat.id, "Выберите филиал 📌 :", reply_markup = adres)


						if message.text == "Мои данные 🔐":
							qr = start.danniy(x = str(message.chat.id))
							ar = open('qrcodes/'+str(qr)+".png", 'rb')
							idd = scan.scanoddiy(x = str(qr))
							#print(idd)
							#print(qr)
							bot.send_photo(message.chat.id, ar, "Ваш QR код !\nВаш GAVALI ID :  "+ str(idd), reply_markup = menyu)


						if message.text == "Контакты 📞":
							bot.send_message(message.chat.id, "Филиал Ц1 📞 :   +998 97 444 11 00\nФилиал Кўкча 📞 :   +998 97 444 22 00", reply_markup = kontakt)

						if message.text == "Мой баланс 💵":
							balans = baza.balans(x = str(message.chat.id))
							balans = tochka.tochka(x = str(balans))
							bot.send_message(message.chat.id, "На вашем счету : "+ str(balans)+" Gavali монеток")

						if message.text != "Адреса магазинов 📍" and message.text != "Мои данные 🔐" and message.text != "Контакты 📞" and message.text != "Мой баланс 💵":
							bot.send_message(message.chat.id, "Выберите одну из действий !", reply_markup = menyu)



				############################# UZBEK KLIENT
				if til =="Узбек тили":
					print(message.text)
					if message.text == "Магазинлар адреси 📍":
						print("ishladi")
						bot.send_message(message.chat.id, "Филиални танланг 📌 :", reply_markup = adresuz)

					if message.text == "Менинг маълумотларим 🔐":
						qr = start.danniy(x = str(message.chat.id))
						ar = open('qrcodes/'+str(qr)+".png", 'rb')
						idd = scan.scanoddiy(x = str(qr))
						#print(idd)
						#print(qr)
						bot.send_photo(message.chat.id, ar, "Сизнинг QR код !\nСизнинг GAVALI ID :  "+ str(idd), reply_markup = menyuuz)


					if message.text == "Контактлар 📞":
						bot.send_message(message.chat.id, "Филиал Ц1 📞 :   +998 97 444 11 00\nФилиал Кўкча 📞 :   +998 97 444 22 00", reply_markup = kontaktuz)

					if message.text == "Менинг балансим 💵":
					    balans = baza.balans(x = str(message.chat.id))
					    balans = tochka.tochka(x = str(balans))
					    bot.send_message(message.chat.id, "Балансингизда : "+ str(balans)+" Gavali тангаси")

					if message.text != "Магазинлар адреси 📍" and message.text != "Менинг маълумотларим 🔐" and message.text != "Контактлар 📞" and  message.text != "Менинг балансим 💵" :
						bot.send_message(message.chat.id, "Буюруклардан бирини босинг !", reply_markup = menyuuz)

		rasm = 0




		###########################################
		def VAR(message):
			global rasm
			if message.text == "По QR код или Gavali ID!":
				bot.send_message(message.chat.id, "Сфотографируйте и отправьте QR код \nИли напишите Gavali ID (AA123456) !", reply_markup=None)
				bot.register_next_step_handler(message, SCAN )
				rasm = 1
			if message.text == "По номеру телефона !":
				bot.send_message(message.chat.id, "Напишите номер телефона !\nПример: +998909000751 !")
				bot.register_next_step_handler(message, NOM )

			if message.text == "Главное меню !":
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

		def NOM(message):  ####### KASSSIIIRRR    KASSIR
			global kassir1
			if "+" in message.text:
				a,b,c = scan.qushish2(x = str(message.text))
				if str(a) != "":
					c = tochka.tochka(x = str(c))
					bot.send_message(message.chat.id, "Имя клиента : "+str(a)+"\nНомер клиента : "+str(message.text)+  "\nGavali id : "+str(b)  + "\nНа балансе клиента : " + str(c)+" Gavali монеток")
					bot.send_message(message.chat.id, "Введите полную сумму покупки : ", reply_markup = otm)
					kassir1 = str(b)
					bot.register_next_step_handler(message, DOB )
				else:
					bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)


			if message.text == "По QR код или Gavali ID!":
				bot.send_message(message.chat.id, "Сфотографируйте и отправьте QR код \nИли напишите Gavali ID (AA123456) !", reply_markup=None)
				bot.register_next_step_handler(message, SCAN )
				rasm = 1
			if message.text == "По номеру телефона !":
				bot.send_message(message.chat.id, "Напишите номер телефона !\nПример: +998909000751 !")
				bot.register_next_step_handler(message, NOM )
			if message.text == "Главное меню !":
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)



		def SCAN(message): ####### KASSSIIIRRR    KASSIR
			global kassir1
			try:
				name = message.chat.id
				try:
					print(message.photo[0].file_id)
					file_info = bot.get_file(message.photo[0].file_id)
					downloaded_file = bot.download_file(file_info.file_path)
					src = str(name)+".png"
					with open(src, 'wb') as new_file:
					    new_file.write(downloaded_file)
					a = scan.scan(x = str(name)) #Gacali id топиб беряпти
					print(a)
					y  = a
					aq,b,c = scan.qushish(x = str(y))
					print(a, b,c)
					if str(aq) != "":
						c = tochka.tochka(x = str(c))
						bot.send_message(message.chat.id, "Имя клиента : "+str(aq)+"\nНомер клиента : "+str(b)+  "\nGavali id : "+str(y)  + "\nНа балансе клиента : " + str(c)+" Gavali монеток")
						bot.send_message(message.chat.id, "Введите полную сумму покупки : ", reply_markup = otm)

						kassir1 = str(y)
						bot.register_next_step_handler(message, DOB )
					else:
						bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

				except Exception:
					if "AA" in message.text :
						print("normroq")
						y  = message.text
						a,b,c = scan.qushish(x = str(y))
						print(a, b,c)
						if str(a) != "":
							c = tochka.tochka(x = str(c))
							bot.send_message(message.chat.id, "Имя клиента : "+str(a)+"\nНомер клиента : "+str(b)+  "\nGavali id : "+str(message.text)  + "\nНа балансе клиента : " + str(c)+" Gavali монеток")

							bot.send_message(message.chat.id, "Введите полную сумму покупки : ", reply_markup = otm)
							kassir1 = str(y)
							bot.register_next_step_handler(message, DOB )
						else:
							bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

					if message.text == "По QR код или Gavali ID!":
						bot.send_message(message.chat.id, "Сфотографируйте и отправьте QR код \nИли напишите Gavali ID (AA123456) !", reply_markup=None)
						bot.register_next_step_handler(message, SCAN )
						rasm = 1
					if message.text == "По номеру телефона !":
						bot.send_message(message.chat.id, "Напишите номер телефона !\nПример: +998909000751 !")
						bot.register_next_step_handler(message, NOM )

					if message.text == "Главное меню !":
						bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

			except Exception:
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

		def DOB(message):  ####### KASSSIIIRRR    KASSIR
			global kassir1
			if message.text != "Отменить":
				summa = message.text
				if "." in message.text or " " in message.text:
					summa = tochka.tochkaout(x = str(message.text))
				print(message.text)
				print(summa)

				klient,moneta, balans = baza.dob(x = str(kassir1), y = str(summa), z = str(message.chat.id))
				moneta = tochka.tochka(x = str(moneta))
				balans = tochka.tochka(x = str(balans))
				til, ism = baza.findlang(x = str(klient))
				if til == "Русский язык":
					bot.send_message(int(klient), "Вам начислено : "+str(moneta)+"  Gavali монеток\n_____________________\nВаш баланс : "+str(balans)+" Gavali монеток", reply_markup = menyu)
				if til == "Узбек тили":
					bot.send_message(int(klient), "Сизга : "+str(moneta)+"  Gavali тангачалари тушди\n_____________________\nХисобингизда : "+str(balans)+" Gavali тангачалари бор", reply_markup = menyuuz)

				bot.send_message(message.chat.id, "Сумма успешно зачислено !", reply_markup = kassir)
				kassir1 = ""
			else:
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

		######################################################

		def VAR2(message):
			global rasm
			if message.text == "По QR код или Gavali ID!":
				bot.send_message(message.chat.id, "Сфотографируйте и отправьте QR код \nИли напишите Gavali ID (AA123456) !", reply_markup=None)
				bot.register_next_step_handler(message, SCAN2 )
				rasm = 1
			if message.text == "По номеру телефона !":
				bot.send_message(message.chat.id, "Напишите номер телефона !\nПример: +998909000751 !")
				bot.register_next_step_handler(message, NOM2 )

			if message.text == "Главное меню !":
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

		def NOM2(message):  ####### KASSSIIIRRR    KASSIR
			global kassir1
			pp = 0
			if "+" in message.text :
				pp=1
				a,b,c = scan.qushish2(x = str(message.text))
				if str(a) != "":
					c = tochka.tochka(x = str(c))
					bot.send_message(message.chat.id, "Имя клиента : "+str(a)+"\nНомер клиента : "+str(message.text)+  "\nGavali id : "+str(b)  + "\nНа балансе клиента : " + str(c)+" Gavali монеток")
					bot.send_message(message.chat.id, "Введите полную сумму для оплаты : ", reply_markup = otm)

					kassir1 = str(b)
					bot.register_next_step_handler(message, DOB2 )
				else:
					bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)


			if message.text == "По QR код или Gavali ID!":
				pp=1
				bot.send_message(message.chat.id, "Сфотографируйте и отправьте QR код \nИли напишите Gavali ID (AA123456) !", reply_markup=None)
				bot.register_next_step_handler(message, SCAN2 )
				rasm = 1
			if message.text == "По номеру телефона !":
				pp=1
				bot.send_message(message.chat.id, "Напишите номер телефона !\nПример: +998909000751 !")
				bot.register_next_step_handler(message, NOM2 )
			if message.text == "Главное меню !":
				pp=1
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)
			if pp == 0:
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)


		def SCAN2(message): ####### KASSSIIIRRR    KASSIR
			global kassir1
			try:
				name = message.chat.id
				try:
					print(message.photo[0].file_id)
					file_info = bot.get_file(message.photo[0].file_id)
					downloaded_file = bot.download_file(file_info.file_path)
					src = str(name)+".png"
					with open(src, 'wb') as new_file:
					    new_file.write(downloaded_file)
					a = scan.scan(x = str(name)) #Gacali id топиб беряпти
					print(a)
					y  = a
					aq,b,c = scan.qushish(x = str(y))
					print(a, b,c)
					if str(aq) != "":
						c = tochka.tochka(x = str(c))
						bot.send_message(message.chat.id, "Имя клиента : "+str(aq)+"\nНомер клиента : "+str(b)+  "\nGavali id : "+str(y)  + "\nНа балансе клиента : " + str(c)+" Gavali монеток")
						bot.send_message(message.chat.id, "Введите полную сумму для оплаты : ", reply_markup = otm)
						kassir1 = str(y)
						bot.register_next_step_handler(message, DOB2 )
					else:
						bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

				except Exception:
					pp = 0
					if "AA" in message.text :
						pp = 1
						print("normroq")
						y  = message.text
						a,b,c = scan.qushish(x = str(y))
						print(a, b,c)
						if str(a) != "":

							summa = tochka.tochka(x = str(c))
							bot.send_message(message.chat.id, "Имя клиента : "+str(a)+"\nНомер клиента : "+str(b)+  "\nGavali id : "+str(message.text)  + "\nНа балансе клиента : " + str(summa)+" Gavali монеток")

							bot.send_message(message.chat.id, "Введите полную сумму для оплаты : ", reply_markup = otm)
							kassir1 = str(y)
							bot.register_next_step_handler(message, DOB2 )
						else:
							bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

					if message.text == "По QR код или Gavali ID!":
						pp=1
						bot.send_message(message.chat.id, "Сфотографируйте и отправьте QR код \nИли напишите Gavali ID (AA123456) !", reply_markup=None)
						bot.register_next_step_handler(message, SCAN2 )
						rasm = 1
					if message.text == "По номеру телефона !":
						pp=1
						bot.send_message(message.chat.id, "Напишите номер телефона !\nПример: +998909000751 !")
						bot.register_next_step_handler(message, NOM2 )

					if message.text == "Главное меню !":
						pp=1
						bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)
					if pp ==0:
						bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

			except Exception:
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

		def DOB2(message):  ####### KASSSIIIRRR    kassir
			global kassir1
			if message.text != "Отменить":
				summa = message.text
				if "." in message.text or " " in message.text :
					summa = tochka.tochkaout(x = str(message.text))


				klient, klientid, kod = baza.oplata1(x = str(kassir1), y = str(summa), z = str(message.chat.id))
				#klient,moneta, balans = baza.oplata(x = str(kassir1), y = str(message.text), z = str(message.chat.id))

				if klient != "Мало денег":
					til, ism = baza.findlang(x = str(klientid))
					print("norm")
					print(til)
					if til == "Русский язык":
						podt = types.InlineKeyboardMarkup(row_width = 2)
						podt1 = types.InlineKeyboardButton(text = "Да", callback_data = kod)
						podt2 = types.InlineKeyboardButton(text = "Нет", callback_data = kod+"нет")
						podt.add(podt1, podt2)
						bot.send_message(int(klientid), "Счёт был оплачен "+str(message.text)+" Gavali монеток\nПодтвердите действие ", reply_markup = podt)
						bot.send_message(message.chat.id, "Сумма будет оплачена после подтверждения клиента !", reply_markup = kassir)
						kassir1 = ""
					if til == "Узбек тили":
						podt = types.InlineKeyboardMarkup(row_width = 2)
						podt1 = types.InlineKeyboardButton(text = "Ха", callback_data = kod)
						podt2 = types.InlineKeyboardButton(text = "Йўк", callback_data = kod+"нет")
						podt.add(podt1, podt2)

						bot.send_message(int(klientid), "Хисобни "+str(message.text)+" Gavali тангачалари билан тўлашни тасдиклайсизми ?", reply_markup = podt)
						bot.send_message(message.chat.id, "Сумма будет оплачена после подтверждения клиента !", reply_markup = kassir)
						kassir1 = ""
				else:
					bot.send_message(message.chat.id, "На счёту клиента мало денег !")
					bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)

			else:
				bot.send_message(message.chat.id, "Выберите одну из действий ", reply_markup = kassir)





		#######################          REGISTRATSIYA



		def FIO(message):
			global nomer, reguz
			nomer2 = nomer
			if message.text == "Отменить":
				baza.otmena(x = str(nomer2), y = "B")
				bot.send_message(message.chat.id, "Отменено", reply_markup = regru)
				print("otmena")
			if message.text == "Бекор килиш !":
				baza.otmena(x = str(nomer2), y = "B")
				bot.send_message(message.chat.id, "Бекор килинди", reply_markup = reguzz)
				#reguz.remove(str(message.chat.id))

			if message.text != "Отменить" and message.text != "Бекор килиш !":
				print("asfafsk")
				text = str(message.text)
				chatid2 = message.chat.id
				start.qushish(x = str(text), y = str(chatid2))
				#time.sleep(1)
				if str(message.chat.id) in reguz:
					baza.changelang(x = str(message.chat.id), y = "uz")

					bot.send_message(message.chat.id, "Руйхатдан утиш муваффакиятли якунланди ✅", reply_markup = None)
					idd = generate.generateqr(nomer = str(nomer2), chatid = str(chatid2))

					qr = open("qrcodes/"+str(nomer2)+".png", 'rb')
					print("norm2")
					bot.send_photo(message.chat.id, qr, "Сизнинг QR кодингиз !\nСизнинг GAVALI ID :  "+ str(idd), reply_markup = menyuuz)
					bot.send_message(message.chat.id, """Табриклаймиз!!! 🎊
илк бора руйхатдан утганингиз туфайли, сизга 15.000 Gavali тангачалари 💎 бонус тарикасида такдим этилди
____
1 Gavali тангачаси = 1 сум""", reply_markup = menyuuz)
					#bot.send_message(message.chat.id, "",   reply_markup = menyu)
				else:
					baza.changelang(x = str(message.chat.id), y = "ru")
					bot.send_message(message.chat.id, "Регистрация прошла успешно ✅", reply_markup = None)
					idd = generate.generateqr(nomer = str(nomer2), chatid = str(chatid2))

					qr = open("qrcodes/"+str(nomer2)+".png", 'rb')
					print("norm2")
					bot.send_photo(message.chat.id, qr, "Ваш QR код !\nВаш GAVALI ID:  "+ str(idd), reply_markup = None)
					bot.send_message(message.chat.id, """Поздравляем!!! 🎊
Вы получили 15.000 бонусных
Gavali монеток 💎 в честь первой регистрации
____
1 Gavali монета = 1 сўм""", reply_markup = menyu)


		bot.polling(none_stop=True)
	except Exception:
		time.sleep(10)
		continue