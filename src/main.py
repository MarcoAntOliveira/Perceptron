import speech_recognition as sr
import pyttsx3

# # Inicializa o reconhecedor de voz
# r = sr.Recognizer()

# # Função para converter texto em fala
# def SpeakText(command):
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()

# # Loop infinito para capturar voz do usuário
# while True:
#     try:
#         # Usa o microfone como fonte de entrada
#         with sr.Microphone() as source:
#             print("Ajustando ruído ambiente. Aguarde um momento...")
#             r.adjust_for_ambient_noise(source, duration=0.5)
#             print("Pode falar agora...")

#             # Escuta o áudio do usuário
#             audio = r.listen(source)

#             # Usa o Google para reconhecer o áudio
#             MyText = r.recognize_google(audio, language='pt-BR')  # ou 'en-US' para inglês
#             MyText = MyText.lower()

#             print("Você disse:", MyText)
#             SpeakText(MyText)

#     except sr.RequestError as e:
#         print(f"Erro ao requisitar resultados do serviço de reconhecimento: {e}")

#     except sr.UnknownValueError:
        # print("Não foi possível entender o áudio. Tente novamente.")
robo = pyttsx3.init()
msg_robo = input('escreva algo: ')
robo.say(msg_robo)
robo.runAndWait()
