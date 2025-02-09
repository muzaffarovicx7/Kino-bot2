from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from states.kino_states import KinoState
from aiogram.fsm.context import FSMContext
from data.config import admin
from buttons.inline_button import tasdiqlash
from database.main import KinoAdd



kino_admin = Router()


@kino_admin.message(F.text == "Add", F.from_user.id.in_(admin))
async def KinoQoshish(mess: Message, state: FSMContext):
    await mess.answer("Qo'shiladigan kino nomini yuboring ...")
    await state.set_state(KinoState.names)



@kino_admin.message(F.text, KinoState.names)
async def KinoDes(mess: Message, state: FSMContext):
    await state.update_data(nomi=mess.text)
    await mess.answer("Kino haqida ma'lumot yuboring ...")
    await state.set_state(KinoState.des)



@kino_admin.message(F.text, KinoState.des)
async def KinoLink(mess: Message, state: FSMContext):
    await state.update_data(des=mess.text)
    await mess.answer("Kinoga link yuboring ...")
    await state.set_state(KinoState.link)



@kino_admin.message(F.text, KinoState.link)
async def KinoEnd(mess: Message, state: FSMContext):
    await state.update_data(link=mess.text)
    data = await state.get_data()
    nomi = data.get("nomi")
    des = data.get("des")
    link = data.get("link")
    await mess.answer(f"Ma'lumotlarni tasdiqlaysizmi?\n\n\n\n🎬 Kino nomi: {nomi}\n\n📁 Haqida: {des}\n\n🔗 Link: {link}", reply_markup=tasdiqlash)
    await state.set_state(KinoState.finish)





@kino_admin.callback_query(F.data, KinoState.finish)
async def KinoTasdiqlash(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    if xabar == "ok":
        data = await state.get_data()
        nomi = data.get("nomi")
        des = data.get("des")
        link = data.get("link")
        KinoAdd(name=nomi, disc=des, link=f"{link}")
        await call.answer("Kino qo'shildi.", show_alert=True)
        await state.clear()
    else:
        await call.answer("Kinoni qo'shish bekor qilindi.", show_alert=True)
        await state.clear()


