import telebot
from telebot import types

#1628570563:AAHJOGY9RZh1pgZO21n2nrNyhqKi5S9NJnc

bot = telebot.TeleBot('1628570563:AAHJOGY9RZh1pgZO21n2nrNyhqKi5S9NJnc')


t = 0 #коэффециент травма
t = int(t)
b = 0 #коэффециент болезни
b = int(b)
z = 0 #коэффециент забитости
z = int(z)
d = 0 #коэффециент дикости
d = int(d)

text_step_1_a = 'Посплю прямо на земле в своем укромном месте, меня зато никто не достанет'
text_step_1_b = 'Поищу где можно отогреться в округе'
text_step_1_w = 'Попробую спрятаться в подъезде, где меня подкармливает консьержка'

text_step_2_a = 'Съем кусок мяса, оставленный около дерева'
text_step_2_b = 'Я знаю одну мусорку, поищу там объедки'
text_step_2_w = 'Пойду попрошайничать в парке'

text_step_2_1_a = 'Милая читающая девушка'
text_step_2_1_b = 'Парень играющий в смартфон'
text_step_2_1_w = 'Бабушка с пакетом кошачьего корма'

text_step_3_a = 'Пробуете подружиться, вместе больше шансов выжить'
text_step_3_b = 'Кажется у них есть еда, пытаетесь стащить кусочек'
text_step_3_w = 'Избигаете их'

text_step_4_a = 'Приветственно виляете хвостом'
text_step_4_b = 'Строите глазки, можете накормить'
text_step_4_w = 'Пытаетесь убежать от него'
text_step_4_q = 'Игнорируте'
text_step_4_e = 'Пытаетесь спрятаться, вам страшно'

text_step_5_a = 'Вам очень нравиться в приюте'
text_step_5_b = 'Вам по началу не нравилось в приюте, но потом вы поняли, что здесь классно'
text_step_5_w = 'Вам не очень нравиться в приюте. но лучше быть здесь'

text_step_6_a = 'Человек особенный'
text_step_6_b = 'Человек обычный'

text_step_6_av1 = 'Скромно сидим'
text_step_6_bv1 = 'Неитерсно. Пытаемся играть с другими псами'
text_step_6_wv1 = 'Радостно лаем, виляем хвостом'

text_step_6_av2 = 'Скромно сидим'
text_step_6_bv2 = 'Неинтерсно. Пытаемся играть с другими псами'
text_step_6_wv2 = 'Чужие люди напрягают, страшно'
text_step_6_qv2 = 'Радостно лаем, виляем хвостом'



def step_0():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Да')
    key2 = types.KeyboardButton('Нет')
    markup.add(key1)
    markup.add(key2)
    return markup

def step_1():
    
    global text_step_1_a
    global text_step_1_b
    global text_step_1_w
    
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_1_a)
    key2 = types.KeyboardButton(text_step_1_b)
    key3 = types.KeyboardButton(text_step_1_w)
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    return markup

def step_2():

    global text_step_2_a
    global text_step_2_b
    global text_step_2_w

    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_2_a)
    key2 = types.KeyboardButton(text_step_2_b)
    key3 = types.KeyboardButton(text_step_2_w)
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    return markup

def step_2_1():

    global text_step_2_1_a
    global text_step_2_1_b
    global text_step_2_1_w
    
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_2_1_a)
    key2 = types.KeyboardButton(text_step_2_1_b)
    key3 = types.KeyboardButton(text_step_2_1_w)
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    return markup

def step_3():

    global text_step_3_a
    global text_step_3_b
    global text_step_3_w
    
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_3_a)
    key2 = types.KeyboardButton(text_step_3_b)
    key3 = types.KeyboardButton(text_step_3_w)
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    return markup

def step_4v1():
    global text_step_4_a
    global text_step_4_b

    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_4_a)
    key2 = types.KeyboardButton(text_step_4_b)
    markup.add(key1)
    markup.add(key2)
    return markup

def step_4v2():
    global text_step_4_w
    global text_step_4_q

    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_4_w)
    key2 = types.KeyboardButton(text_step_4_q)
    markup.add(key1)
    markup.add(key2)
    return markup

def step_5():
    global text_step_5_a
    global text_step_5_b
    global text_step_5_w

    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_5_a)
    key2 = types.KeyboardButton(text_step_5_b)
    key3 = types.KeyboardButton(text_step_5_w)
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    return markup

def step_6():
    
    global text_step_6_a
    global text_step_6_b
    
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_6_a)
    key2 = types.KeyboardButton(text_step_6_b)
    markup.add(key1)
    marlup.add(key2)
    return markup

def step_6v1():
    
    global text_step_6_av1
    global text_step_6_bv1
    global text_step_6_wv1
    
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_6_av1)
    key2 = types.KeyboardButton(text_step_6_bv1)
    key3 = types.KeyboardButton(text_step_6_wv1)
    markup.add(key1)
    marlup.add(key2)
    marlup.add(key3)
    return markup

def step_6v2():
    
    global text_step_6_av2
    global text_step_6_bv2
    global text_step_6_wv2
    global text_step_6_qv2
    
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(text_step_6_av2)
    key2 = types.KeyboardButton(text_step_6_bv2)
    key3 = types.KeyboardButton(text_step_6_wv2)
    key4 = types.KeyboardButton(text_step_6_qv2)
    markup.add(key1)
    marlup.add(key2)
    marlup.add(key3)
    marlup.add(key4)
    return markup

@bot.message_handler(content_types = ['text'])
def get_start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id,
        'Здравствуй!\n'+
        'Приветствуем тебя в нашей интерактивной игре ДАЙ ЛАПУ!\n'+
        'Данная игра представляет из себя вариативную текстовую игру, где ты погрузишься в жизнь бездомного пса!\n'+
        'Давай начнем!)\n', reply_markup = step_0())
    if message.text == 'Да':
        bot.send_message(message.from_user.id, 'Ты готов?')
        bot.register_next_step_handler(message, get_step_1)
    elif message.text == 'Нет':
        bot.send_message(message.from_user.id, 'Очень жаль!')

def get_step_1(message): 
    if message.text == 'Да':
        bot.send_message(message.from_user.id, 'Действие 1: На улице ударил холод, да и еще и дождь. Вы промокли насквозь и ищете, где укрыться.\n'+'Какие ваши действия?', reply_markup = step_1())
        bot.register_next_step_handler(message, get_step_11)
    else:
        bot.send_message(message.from_user.id, 'Игра не начнеться, пока ты не будешь готов!')
        
def get_step_11(message):

    global t
    global b
    global z
    global d
    
    global text_step_1_a
    global text_step_1_b
    global text_step_1_w

    if message.text == text_step_1_a:
        bot.send_message(message.from_user.id, 'Вы пережили ночь, но чувствуете себя хуже, чем вчера')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_2')
        b = b + 1
        d = d + 1
        bot.register_next_step_handler(message, get_step_2)
    elif message.text == text_step_1_b:
        bot.send_message(message.from_user.id, 'Вы заснули под теплыми трубами, пока вы не выросли и помещаетесь под ними - можете здесь греться')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_2')
        z = z + 1
        d = d + 1
        bot.register_next_step_handler(message, get_step_2)
    elif message.text == text_step_1_w:
        bot.send_message(message.from_user.id, 'Консьержка пустила вас и вы немного погрелись, но жильцы, увидевшие вас, пинками выгнали из подъезда')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_2')
        t = t + 1
        z = z + 1
        d = d + 1
        bot.register_next_step_handler(message, get_step_2)
    else:
        bot.send_message(message.from_user.id, 'Выберите один из вариантов!')

def get_step_2(message):
    if message.text == '\действие_2':
        bot.send_message(message.from_user.id, 'Действие 2: Это был долгий день, и вы очень голодны.\n'+'Куда пойдете искать еду?', reply_markup = step_2())
        bot.register_next_step_handler(message, get_step_21)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю! Напишите команду \действие_2')

def get_step_21(message):

    global t
    global b
    global z
    global d
        
    global text_step_2_a
    global text_step_2_b
    global text_step_2_w

    if message.text == text_step_2_a:
        bot.send_message(message.from_user.id, 'Вас отравили догхантеры!')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_3')
        t = t + 3
        d = d + 3
        b = b + 3
        bot.register_next_step_handler(message, get_step_3)
    elif message.text == text_step_2_b:
        bot.send_message(message.from_user.id, '---')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_3')
        z = z + 1
        d = d + 1
        bot.register_next_step_handler(message, get_step_3)
    elif message.text == text_step_2_w:
        bot.send_message(message.from_user.id, 'В парке много людей и вы не знаете, к кому подойти', reply_markup = step_2_1())
        bot.register_next_step_handler(message, get_step_22)
        
def get_step_22(message):

    global t
    global b
    global z
    global d
    
    global text_step_2_1_a
    global text_step_2_1_b
    global text_step_2_1_с
    
    if message.text == text_step_2_1_a:
        bot.send_message(message.from_user.id, 'Девушка вас испугалась, и прогнала!')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_3')
        z = z + 1
        d = d + 1
        bot.register_next_step_handler(message, get_step_3)
    elif message.text == text_step_2_1_b:
        bot.send_message(message.from_user.id, 'Парень бросил в вас камень!')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_3')
        t = t + 1
        z = z + 1
        d = d + 1
        bot.register_next_step_handler(message, get_step_3)
    else:
        bot.send_message(message.from_user.id, 'Бабушка вас покормила!')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_3')
        bot.register_next_step_handler(message, get_step_3)

def get_step_3(message):
    if message.text == '\действие_3':
        bot.send_message(message.from_user.id, 'Действие 3: Вы замечаете собак вашего размера.\n'+'Ваши действия?', reply_markup = step_3())
        bot.register_next_step_handler(message, get_step_31)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю! Напишите команду \действие_3')
        bot.register_next_step_handler(message, get_step_3)

def get_step_31(message):

    global t
    global b
    global z
    global d

    global text_step_3_a
    global text_step_3_b
    global text_step_3_w

    if message.text == text_step_3_a:
        bot.send_message(message.from_user.id, 'Теперь вы сторонитесь людей, вам комфортно в бездомной стае')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_4')
        d = d + 1
        bot.register_next_step_handler(message, get_step_4)
    elif message.text == text_step_3_b:
        bot.send_message(message.from_user.id, 'Началась драка, в которой вы проиграли')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_4')
        t = t + 1
        z = z + 1
        d = d + 1
        bot.register_next_step_handler(message, get_step_4)
    elif message.text == text_step_3_w:
        bot.send_message(message.from_user.id, 'Избигаете их')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_4')
        z = z + 1
        d = d + 1
        bot.register_next_step_handler(message, get_step_4)

def get_step_4(message):
    
    global d
    
    if message.text == '\действие_4':
        if (d >= 0)and(d < 3)and(d != 1):
            bot.send_message(message.from_user.id, 'Действие 4: Вы случайно натыкаетесь на человека, который подзывает вас к себе.\n'+'Ваши действия?', reply_markup = step_4v1())
            bot.register_next_step_handler(message, get_step_41v1)
        elif (d != 1)and(d > 2):
            bot.send_message(message.from_user.id, 'Действие 4: Вы случайно натыкаетесь на человека, который подзывает вас к себе.\n'+'Ваши действия?', reply_markup = step_4v2())
            bot.register_next_step_handler(message, get_step_41v2)
        elif (d == 1):
            bot.send_message(message.from_user.id, 'Действие 4: Вы случайно натыкаетесь на человека, который подзывает вас к себе.\n'+'Ваши действия?', reply_markup = step_4v2())
            bot.register_next_step_handler(message, get_step_41v2)

def get_step_41v1(message):
    
    global t
    global b
    global z
    global d

    global text_step_4_a
    global text_step_4_b

    if message.text == ((text_step_4_a)or(text_step_4_b)):
        bot.send_message(message.from_user.id, 'В приюты попадают только самые социальные животные с улицы, меньше 10%, и им все равно требуется помощь зоопсихолога.\n'+
                         'На данный момент уровень ваших параметров:\n'+
                         'Травмы: ' + str(t) + '\n' +
                         'Болезнь: ' + str(b) + '\n' +
                         'Забитость: ' + str(z) + '\n' +
                         'Дикость: ' + str(d))
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему шагу, напишите команду \действие_5')
        bot.register_next_step_handler(message, get_step_5)

def get_step_41v2(message):

    global t
    global b
    global z
    global d

    global text_step_4_w
    global text_step_4_q
    global text_step_4_e

    if message.text == ((text_step_4_w)or(text_step_4_q)or(text_step_4_e)):
        bot.send_message(message.from_user.id, 'Вас стерилизовали и выпустили на свободу. Игра окончена!\n'+
                        'Ваши параметры на момент окночания игры:\n' +
                        'Травмы: ' + str(t) + '\n' +
                        'Болезнь: ' + str(b) + '\n' +
                        'Забитость: ' + str(z) + '\n' +
                        'Дикость: ' + str(d) + '\n')
        bot.send_message(message.from_user.id, 'Чтобы начать игру заново, напишите команду \start')
        bot.register_next_step_handler(message, get_start)

def get_step_5(message):
    if message.text == '\действие_5':
        bot.send_message(message.from_user.id, 'Действие 5: Вы попали в приют. Здесь для вас проводят лечение, с вами работают волонтеры, постонное питание.', reply_markup = step_5())
        bot.register_next_step_handler(message, get_step_5_1)

def get_step_5_1(message):

    global t
    global b
    global z
    global d

    t = 0
    b = 0
    z = z - 1
    d = d - 2

    global text_step_5_a
    global text_step_5_b
    global text_step_5_w

    bot.send_message(message.from_user.id, 'Что вы думаете об этом?', reply_markup = step_5())
    if message.text == ((text_step_5_a)or(text_step_5_b)or(text_step_w)):
        bot.send_message(message.from_user.id, 'Дейсвие 6: Вы привыкли к приюту, но вдруг появляеться человек' +
                         'Ваши параметры в приюте:\n' +
                         'Травмы: ' + str(t) + '\n' +
                         'Болезнь: ' + str(b) + '\n' +
                         'Забитость: ' + str(z) + '\n' +
                         'Дикость: ' + str(d))
        bot.register_next_step_handler(message, get_step_6)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю, выбирете действие из предложеных!')
        bot.register_next_step_handler(message, get_step_5)

def get_step_6(message):
    bot.send_message(message.from_user.id, 'Какой это человек?', reply_markup = step_6())
    bot.register_next_step_handler(message, get_step_6_e)

def get_step_6_e(message):

    global text_step_6_a
    global text_step_6_b
    
    if message.text == text_step_6_a:
        bot.send_message(message.from_user.id, 'К вам пришел человек особенный!')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему действия напишите команду \действие_7_в1')
        bot.register_next_step_handler(message, get_step_6v1)
    elif message.text == text_step_6_b:
        bot.send_message(message.from_user.id, 'К вам пришел человек обычный!')
        bot.send_message(message.from_user.id, 'Чтобы перейти к следующему действия напишите команду \действие_7_в2')
        bot.register_next_step_handler(message, get_step_6v2)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю, ответьте на вопрос выбрав ответ из предложенных')
        bot.register_next_step_handler(message, get_step_6)

def get_step_6v1(message):
    
    global text_step_6_av1
    global text_step_6_bv1
    global text_step_6_wv1

    if message.text == ((text_step_6_av1)or(text_step_6_bv1)):
        bot.send_message(message.from_user.id, 'Остаток своей жизни вы проведете в приюте. Но у вас появился человек, который будет вашим опекуном!')
        bot.send_message(message.from_user.id, 'Игра окончена! Если хотите сыграть еще раз, то напишите команду /start')
        bot.register_next_step_handler(message, get_start)
    elif message.text == text_step_6_wv1:
        bot.send_message(message.from_user.id, 'Вы и этот человек, очень подружились! Теперь вы лучшие друзья!!')
        bot.send_message(message.from_user.id, 'Игра окончена! Если хотите сыграть еще раз, то напишите команду /start')
        bot.register_next_step_handler(message, get_start)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю, ответьте на вопрос выбрав ответ из предложенных')
        bot.register_next_step_handler(message, get_step_6)

def get_step_6v2(message):

    global text_step_6_av2
    global text_step_6_bv2
    global text_step_6_wv2
    global text_step_6_qv2

    if message.text == ((text_step_6_av2)or(text_step_6_bv2)or(text_step_6_wv2)):
        bot.send_message(message.from_user.id, 'Остаток своей жизни вы проведете в приюте!')
        bot.send_message(message.from_user.id, 'Игра окончена! Если хотите сыграть еще раз, то напишите команду /start')
        bot.register_next_step_handler(message, get_start)
    elif message.text == text_step_6_qv2:
        bot.send_message(message.from_user.id, 'Вы и этот человек, очень подружились! Теперь вы лучшие друзья!!')
        bot.send_message(message.from_user.id, 'Игра окончена! Если хотите сыграть еще раз, то напишите команду /start')
        bot.register_next_step_handler(message, get_start)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понимаю, ответьте на вопрос выбрав ответ из предложенных')
        bot.register_next_step_handler(message, get_step_6)
        
            
bot.polling()
