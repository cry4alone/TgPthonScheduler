from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router, F
import app.keyboard as kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router = Router()

class FSM_States(StatesGroup):
    waiting_for_text = State()
    waiting_for_date = State()
    waiting_for_time = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Это бот-напоминалка, ты можешь устанавливать себе напоминания. Выбери пункт меню ниже для желаемого действия', reply_markup=kb.main)

@router.message(F.text == "Создать напоминание")
async def create_reminder(message: Message, state: FSMContext):
    await message.answer("Введите текст напоминания:", reply_markup=None)
    await state.set_state(FSM_States.waiting_for_text)

@router.message(FSM_States.waiting_for_text)
async def process_waiting_for_text_state(state: FSMContext, message: Message):
    async with state.proxy() as data:
        data['reminder_text'] = message.text
    await message.answer("Введите дату напоминания в формате ДД.ММ.ГГ")
    await state.set_state(FSM_States.waiting_for_date)

@router.message(FSM_States.waiting_for_date)
async def process_waiting_for_date_state(state: FSMContext, message: Message):
    async with state.proxy() as data:
        data['reminder_date'] = message.text
    await message.answer("Введите время напоминания в формате ЧЧ.ММ")
    await state.set_state(FSM_States.waiting_for_time)