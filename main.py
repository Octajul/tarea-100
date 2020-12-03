# Variable para llevar a cabo un limite de diferencia mayor entre sensores de luz
diff = 100
#Mostrar una imagen de cara dormida
basic.show_icon(IconNames.ASLEEP)
#input.button_is_pressed(Button.A)
#input.button_is_pressed(Button.B)
#Parar el bot si estaba en movimiento
gigglebot.stop()
#Definir velocidad de movimiento de los motores
gigglebot.set_speed(gigglebotWhichMotor.BOTH, 50)
#Loop principal
while True:
    #Definir accion si boton A se presiona
    if input.button_is_pressed(Button.A):
        #Mostrar imagen de corazon
        basic.show_icon(IconNames.HEART)
        #Entrar en nuevo Loop
        while True:
            # Mostrar cara feliz
            basic.show_icon(IconNames.HAPPY)
            #Leer sensores de luz 
            right=gigglebot.light_read_sensor(gigglebotWhichTurnDirection.RIGHT)
            left=gigglebot.light_read_sensor(gigglebotWhichTurnDirection.LEFT)
            # Ver si un sensor capta mayor luz que el otro 
            #Si derecha capta mas que izquiera girar a la derecha
            if right > left+diff:
                gigglebot.turn(gigglebotWhichTurnDirection.RIGHT)
            #Si capta mas izquierda girar a la izquierda
            elif left > right+diff:
                gigglebot.turn(gigglebotWhichTurnDirection.LEFT)
            #Si captan similar ir recto
            else:
                gigglebot.drive_straight(gigglebotWhichDriveDirection.FORWARD)
            #Si el boton B es presionado salir del loop y detener el robot y mostrar cara dormida
            if input.button_is_pressed(Button.B):
                gigglebot.stop()
                basic.show_icon(IconNames.ASLEEP)
                break
