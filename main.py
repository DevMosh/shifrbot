from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.types import Message

from keyboard import *
from shifr import *

list_shift = ['Цезарь', 'Виженера', 'Атбаш', 'Трисемиус', 'Полибианский квадрат', 'Биграмный', 'Гронсфельда']


class FSMFillForm(StatesGroup):
    word = State()  # сюда слово для шифрования / дешифрования
    key = State()  # сюда код
    # fill_gender = State()      # Состояние ожидания выбора пола
    # upload_photo = State()     # Состояние ожидания загрузки фото
    # fill_education = State()   # Состояние ожидания выбора образования
    # fill_wish_news = State()   # Состояние ожидания выбора получать ли новости

# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text='Добро пожаловать в бот! Выберите нужный тип шифровки: ', reply_markup=start_menu())


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text='/help')


@router.message(F.text.in_(['🔐', '🔓']))
async def shifr_func(message: Message, state: FSMContext):
    await state.update_data(shifr_deshifr=message.text)
    await message.answer('Какой шифр хотите использовать?', reply_markup=shifr_menu())


@router.message(F.text.in_(list_shift))
async def chezar_func(message: Message, state: FSMContext):
    await state.update_data(name_shifr=message.text)
    await message.answer("введите текст:")
    if message.text == 'Атбаш':
        await state.set_state(FSMFillForm.key)
    else:
        await state.set_state(FSMFillForm.word)


@router.message(StateFilter(FSMFillForm.word), F.text.isalpha())
async def process_word_sent(message: Message, state: FSMContext):
    await state.update_data(word=message.text)
    data_state = await state.get_data()
    if data_state['name_shifr'] in ['Цезарь', 'Полибианский квадрат']:
        await message.answer(text='Спасибо!\n\nА теперь введите цифру:', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(FSMFillForm.key)
    elif data_state['name_shifr'] in ['Виженера']:
        await message.answer(text='Спасибо!\n\nА теперь введите слово:', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(FSMFillForm.key)


@router.message(StateFilter(FSMFillForm.key))
async def process_key_sent(message: Message, state: FSMContext):
    print('test')
    data_state = await state.get_data()

    # word = ''
    # if data_state['name_shifr'] == 'Атбаш':
    #     pass
    # else:
    word = data_state['word'].upper()

    key = message.text
    text = 'Ваш текст: '

    if data_state['shifr_deshifr'] == '🔐':  # шифрование
        if data_state['name_shifr'] == 'Цезарь':
            text = caesar_cipher(word=word, key=int(key))
        if data_state['name_shifr'] == 'Виженера':
            text = vigener_cipher(word=word, key=key)
        if data_state['name_shifr'] == 'Атбаш':
            text = atbash_cipher(word=key)
        if data_state['name_shifr'] == 'Полибианский квадрат':
            text = polybian_square_cipher(word=word, key=key)

    if data_state['shifr_deshifr'] == '🔓':  # шифрование
        if data_state['name_shifr'] == 'Цезарь':
            text = decrypt_caesar_cipher(word=word, key=int(key))
        if data_state['name_shifr'] == 'Виженера':
            text = decrypt_vigener_cipher(word=word, key=key)
        if data_state['name_shifr'] == 'Атбаш':
            text = atbash_cipher(word=key)
        if data_state['name_shifr'] == 'Полибианский квадрат':
            text = decrypt_polybian_square_cipher(word=word, key=key)

    await message.answer(text=f'Готово!\n\n{text}', reply_markup=start_menu())
    await state.clear()


@router.message(F.text == '🔙 Назад')
async def shifr_func(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Главное меню', reply_markup=start_menu())