from IMGCONVERTER import frontend
from PIL import Image
import os
import winotify


def change_appearance_mode_event(new_appearance_mode: str):
    frontend.ct.set_appearance_mode(new_appearance_mode)


def botaodiretorio():
    local = frontend.filedialog.askdirectory()
    frontend.label_direscolhido.configure(text=local)


def converter():
    imagem = frontend.filedialog.askopenfilename()
    extensao = frontend.combobox_conversao.get()
    arquivo = Image.open(f"{imagem}").convert("RGB")
    local = frontend.label_direscolhido.cget("text")
    arquivo.save(f"{local}/img_convert.{extensao}", format=extensao)

    notificacao = winotify.Notification(
        app_id="APP CONVERSOR DE IMAGENS",
        title="NOTIFICAÇÃO",
        msg="Conversão Concluída Com Sucesso!!!",
        duration="long",
        icon=os.path.dirname(os.path.abspath(__file__))+"/convertok.ico"
    )
    notificacao.set_audio(winotify.audio.Default, loop=False)
    notificacao.show()