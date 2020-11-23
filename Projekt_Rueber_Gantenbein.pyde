#Listen definieren
listeX = []
listeY = []
listeZ = []

#Button platzieren
x = 690
y = 540

#Gitternetz einblenden
def setup():
    size(900, 600) 
    clearScreen()
    
#Zeichnen (Quelle: Hefti und Schlegel)
def draw():
        if mousePressed == True and mouseX <= 450 and mouseY <= 600:

            if mouseButton == LEFT:
                stroke(0, 0, 0)
            if mouseButton == RIGHT:
                stroke(255, 0, 0)
            if mouseButton == CENTER:
                stroke(0, 0, 255)
            
#Quelle: Hefti und Schlegel            
#Button       
        if mousePressed == True and mouseX >= x and mouseX <= x + 200 and mouseY >= y and mouseY <= y + 50:
            fill(255, 0, 0)
            clearScreen2()
           
        else:
            fill (60, 60, 60)
        
        rect(x, y, 200, 50)

def clearScreen():
    background(248, 187, 208) 
    stroke(0, 0, 0) 
    textSize(20) 
    strokeWeight(4) 
    line(450,0,450,600) 
    gitternetz()

def clearScreen2():
    background(248, 187, 208) 
    stroke(0, 0, 0) 
    textSize(20) 
    strokeWeight(4) 
    line(450,0,450,600) 
    gitternetz()
    
    for i in range(len(listeX)):
        listeX.pop(-1)
        listeY.pop(-1)
        listeZ.pop(-1)
        
#Punkte
def mousePressed(): 

    if mouseX <= 450 and mouseY <= 600: 
        fill(30, 30, 0) 
        #Linke Punkte
        circle(mouseX, mouseY, 12) 
        #Rechte Punkte
        circle(900 - mouseX, mouseY, 12) 
        
#Koordinaten den jeweiligen Listen hinzufügen
        listeX.append(mouseX) #Koordinaten von x werden der ListeX hinzugefügt
        listeY.append(mouseY) #Koordinaten von y werden der ListeY hinzugefügt
        listeZ.append(900 - mouseX) #Koordinaten der Spiegelung von x werden der ListeZ hinzugefügt
        
#Verbindung der Punkte mit einer Linie
    if len(listeX) > 1: #funktioniert erst, wenn die Länge grösser als 1 ist, weil man bei einem Klick noch keine Linie braucht
        x = len(listeX) - 2
        y = len(listeX) - 1
        line(listeX[x], listeY[x], listeX[y], listeY[y]) #Linien der gezeichneten Figur (links)
        line(listeZ[x], listeY[x], listeZ[y], listeY[y]) #Linien der gespiegelten Figur (rechts)

#Gitternetz        
def gitternetz():
    strokeWeight(1) 
    stroke(230, 30, 100) 
    for y in range (1, 20): 
        line(0,y*30, 900, y*30) 
    for x in range (1,30): 
        line(x*30, 600, x*30, 0) 
