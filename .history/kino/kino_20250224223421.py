import qrcode
import os
from aiogram import F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart, Command
from database.main import ObunachilarAdd, KinoRead, KinoDelete, KinoOlish, Obunachilar
from buttons.inline_button import sorov, knma
from aiogram.fsm.context import FSMContext
from states.kino_states import KinoState
from kino.kino_add import kino_admin
from database.main import KinoAdd
from data.config import admin
from buttons.inline_button import tasdiqlash




kino_router = Router()


@kino_router.message(CommandStart())
async def StartBot(message: Message):
    name = message.from_user.full_name
    id = message.from_user.id
    
    ObunachilarAdd(name=name, id=id)
    rasm = FSInputFile("Jpg/photo_2025-01-16_19-51-37.jpg")
    await message.answer_photo(photo=rasm, caption=f"Assalomu aleykum {name}\n🎬 Kino botga xush kelibsiz!", reply_markup=sorov)


@kino_router.message(Command('obuna'))
async def Obunachilar1(message: Message, state: FSMContext):
    if message.from_user.id in admin:
        obuna = ""
        for i in Obunachilar():
            obuna += f"Ism : {i[1]}\nTelegram 🆔 : {i[2]}\n\n"
        jami = len(Obunachilar())
        await message.answer(f"Sizning obunachilaringiz!\n\n{obuna}\n\nJami obunachilar: {jami}")
    else:
        await message.answer("Siz admin emassiz.")
        await state.clear()
        await message.answer("✍🏻 kino kodini kiriting.")
        await state.set_state(KinoState.qidirish)
        


@kino_router.message(Command("add"))
async def AddKino2(mess: Message, state: FSMContext):
    await mess.answer("Qo'shiladigan kino nomini yuboring ...")
    await state.set_state(KinoState.names)





@kino_router.callback_query(F.data == "qidirkod")
async def Qidirish(call: CallbackQuery, state: FSMContext):
    await call.message.answer("✍🏻 kino kodini kiriting.")
    await state.set_state(KinoState.qidirish)





@kino_router.callback_query(F.data == "qrcode")
async def QrCode(call: CallbackQuery, state: FSMContext):
    # QR kodda bo'ladi yozuv
    await call.message.answer("QR kodda nima bo'lishini yozing ...")
    await state.set_state(KinoState.qr1)



@kino_router.message(F.text, KinoState.qr1)
async def QrCode1(message: Message, state: FSMContext):
    data = message.text
    # QR kodni yaratish
    qr = qrcode.QRCode(
        version=1,  # QR kod hajmi (1 eng kichik, 40 eng katta)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Xatoni tuzatish darajasi
        box_size=10,  # Bir kvadratning o'lchami (piksellarda)
        border=4,  # Chetdagi qirralar (kvadratlarda)
    )

    qr.add_data(data)
    qr.make(fit=True)

    # QR kodni rasmga aylantirish
    img = qr.make_image(fill_color="black", back_color="white")

    # Rasmni saqlash
    img.save("qrcode.png")

    rasm = FSInputFile("qrcode.png")

    await message.answer_photo(photo=rasm, caption="QR kod yaratildi.")
    os.remove("qrcode.png")
    await state.clear()






@kino_router.callback_query(F.data == "admtas")
async def Qidirish1(call: CallbackQuery, state: FSMContext):
    if call.from_user.id in admin:
        await call.message.answer("Kinoni nima qilmoqchisiz?", reply_markup=knma)
        await state.set_state(KinoState.ad)
    else:
        await call.message.answer("Siz admin emassiz.")
        await state.clear()
        await call.message.answer("✍🏻 kino kodini kiriting.")
        await state.set_state(KinoState.qidirish)





@kino_router.callback_query(F.data, KinoState.ad)
async def TassBot(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    if xabar == "KAdd":
        await call.message.answer("Qo'shiladigan kino nomini yuboring ...")
        await state.set_state(KinoState.names)
    else:
        a = ""
        for movie in KinoOlish():
            a += f"🆔: {movie[0]}\nName: {movie[1]}\n\n"
        await call.message.answer(f"{a}\n\nO'chiriladigan kino kodini kiriting ...")
        await state.set_state(KinoState.tass1)





@kino_router.message(F.text, KinoState.tass1)
async def Tass1Bot(mess: Message, state: FSMContext):
    xabar = mess.text
    KinoDelete(id=xabar)
    await mess.answer("Kino o'chirildi.", show_alert=True)
    await state.clear()






# ============================================================================================== >>>>>>>>>>>





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





# ============================================================================================== >>>>>>>>>>>


@kino_router.message(Command("add"))
async def AddKino(message: Message, state: FSMContext):
    if message.from_user.id in admin:
        await message.answer("Qo'shiladigan kino nomini yuboring ...")
        await state.set_state(KinoState.names)
    else:
        await message.answer("Siz admin emassiz.")
        await state.clear()
        await message.answer("✍🏻 kino kodini kiriting.")
        await state.set_state(KinoState.qidirish)








@kino_router.message(F.text, KinoState.qidirish)
async def Kino(message: Message):
    xabar = message.text
    if xabar.isdigit():
        try:
            kino = KinoRead(id=xabar)
            await message.answer_video(video=f"{kino[3]}", caption=f"{kino[1]}\n\n{kino[2]}\n\nAdmin: @laz1zbek0o_o")
        except:
            await message.answer("Kechirasiz, bunday kino topilmadi 🙅‍♂️")
    else:
        await message.answer("Iltimos🙏, kino kodini kiriting 🎬")


