from Scene import Scene
import cv2
import winsound

class Scenes:
    """Scenes Class"""

    txt = ['Él es Javier. Javier es un excéntrico empresario de bienes raíces. Lleva una vida de ensueño en la ciudad\nde Nueva York y cuenta con innumerables inversiones exitosas. Pero un día, todo eso cambió...\nJavier tiene un defecto, no sabe mucho sobre la seguridad en internet. Tu deberás identificar\nsi las acciones de Javier fueron las mejores o si aún tiene cosas que aprender. A través de la historia\nde Javier aprenderás a identificar los riesgos de la navegación en internet.',
            'SÍ, cualquier red de internet me sirve lo importante es reunirme a hablar de trabajo, no hay ningún riesgo',
            'Las cookies son pequeños archivos de texto que\nlos sitios web guardan en tu dispositivo cuando los visitas.\nSirven para almacenar información sobre tu actividad en línea',
            '¡Ups! Parece que has tomado una mala decisión.\n\nEl enlace que acabas de hacer clic no era un bono legítimo, sino una trampa diseñada\npara robar tus datos. Las estafas en línea pueden ser muy\nengañosas, y este tipo de fraude es más común de lo que parece.\n\n¿Por qué es una estafa?\n\n1. Los enlaces que prometen bonos irresistibles suelen ser intentos de robar tu\ninformación personal o financiera.\n\n2. Las empresas legítimas nunca pedirán tus datos por medio de enlaces\no correos sospechosos.',
            '¡Ahora sabes cómo identificar una estafa!\n\nPara avanzar en este juego, asegúrate de tomar decisiones más sabias y proteger tus recursos.\nSi haces clic en ofertas dudosas, podrías perder más que solo dinero.\n\n¡Ten cuidado y no dejes que te engañen, recuerda que lo mejor es DENUNCIAR!']
    
    def __init__(self):
        self.scene = None
        self.head = None
        
    def addScene(self, scene, index):
        """Add A Scene

        Args:
            scene (cv2.VideoCapture): Scene Video
            index (int): Scene Number
        """
        new_scene = Scene(scene, index)
        if self.head is None:
            self.head = new_scene
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_scene

    def getScene(self, index, rr):
        """Play A Scene

        Args:
            index (int): Scene Number
            rr (int): Refresh Rate
        """
        current = self.head
        while current is not None:
            if current.index == index:
                winsound.PlaySound(f'assets/audios/scene{index}.wav', winsound.SND_ASYNC) # Here the audio of the scene is played.
                while True:
                    ret, frame = current.scene.read()
                    if ret:
                        cv2.imshow('El Poder De Un Click', frame)
                        cv2.waitKey(rr)
                    else:
                        break
                cv2.destroyAllWindows()
                break
            current = current.next
