from graphics import*



def main():
    win=GraphWin("scenario", 900,750)
    win.setBackground(color_rgb(70,70,70))

    field=Polygon(Point(0,620), Point(900,620), Point(900,900),Point(0,900))
    field.setFill(color_rgb(36,105,52))


    roadup=Polygon(Point(0,400), Point(900,400), Point(900,420),Point(0,420))
    roadup.setFill(color_rgb(153,76,00))
    road=Polygon(Point(0,400), Point(900,400), Point(900,600),Point(0,600))
    road.setFill(color_rgb(00,0,00))
    roaddown=Polygon(Point(0,600), Point(900,600), Point(900,620),Point(0,620))
    roaddown.setFill(color_rgb(153,76,00))
    roadline1=Polygon(Point(0,500),Point(100,500), Point(100,515),Point(0,515))
    roadline1.setFill(color_rgb(255,255,255))
    roadline2=Polygon(Point(200,500),Point(300,500), Point(300,515),Point(200,515))
    roadline2.setFill(color_rgb(255,255,255))
    roadline3=Polygon(Point(400,500),Point(500,500), Point(500,515),Point(400,515))
    roadline3.setFill(color_rgb(255,255,255))
    roadline4=Polygon(Point(600,500),Point(700,500), Point(700,515),Point(600,515))
    roadline4.setFill(color_rgb(255,255,255))
    roadline5=Polygon(Point(800,500),Point(900,500), Point(900,515),Point(800,515))
    roadline5.setFill(color_rgb(255,255,255))
    x=Point(50,50)
    moon=Circle(x,35)
    moon.setFill(color_rgb(225,187,62))





#building  1

    b1=Polygon(Point(0,200),Point(50,200),Point(50,400),Point(0,400))
    b1.setFill((color_rgb(100,100,100)))



    b1win1 = Polygon(Point(10, 220), Point(40, 220), Point(40, 260), Point(10, 260))
    b1win1.setFill(color_rgb(255,153,51))
    b1win2 = Polygon(Point(10, 280), Point(40, 280), Point(40, 320), Point(10, 320))
    b1win2.setFill(color_rgb(200,200,200))
    b1win3 = Polygon(Point(10, 340), Point(40, 340), Point(40, 380), Point(10, 380))
    b1win3.setFill(color_rgb(200,200,200))
#building 2
    b2=Polygon(Point(50,150),Point(200,150),Point(200,400),Point(50,400))
    b2.setFill((color_rgb(00,100,100)))
    b2win4 = Polygon(Point(70, 200), Point(100, 200), Point(100, 160), Point(70, 160))
    b2win4.setFill(color_rgb(200,200,200))
    b2win1 = Polygon(Point(70, 220), Point(100, 220), Point(100, 260), Point(70, 260))
    b2win1.setFill(color_rgb(200,200,200))
    b2win2 = Polygon(Point(70, 280), Point(100, 280), Point(100, 320), Point(70, 320))
    b2win2.setFill(color_rgb(200,200,200))
    b2win3 = Polygon(Point(70, 340), Point(100, 340), Point(100, 380), Point(70, 380))
    b2win3.setFill(color_rgb(200,200,200))

    b2win5 = Polygon(Point(190, 200), Point(160, 200), Point(160, 160), Point(190, 160))
    b2win5.setFill(color_rgb(200,200,200))
    b2win6 = Polygon(Point(190, 220), Point(160, 220), Point(160, 260), Point(190, 260))
    b2win6.setFill(color_rgb(200,200,200))
    b2win7 = Polygon(Point(190, 280), Point(160, 280), Point(160, 320), Point(190, 320))
    b2win7.setFill(color_rgb(255,153,51))
    b2win8 = Polygon(Point(190, 340), Point(160, 340), Point(160, 380), Point(190, 380))
    b2win8.setFill(color_rgb(200,200,200))

    # building 3
    b3 = Polygon(Point(200, 100), Point(400, 100), Point(400, 400), Point(200, 400))
    b3.setFill((color_rgb(46, 55, 71)))

    b3win1 = Polygon(Point(220, 220), Point(250, 220), Point(250, 260), Point(220, 260))
    b3win1.setFill(color_rgb(255,153,51))
    b3win2 = Polygon(Point(220, 280), Point(250, 280), Point(250, 320), Point(220, 320))
    b3win2.setFill(color_rgb(200, 200, 200))
    b3win3 = Polygon(Point(220, 340), Point(250, 340), Point(250, 380), Point(220, 380))
    b3win3.setFill(color_rgb(255,153,51))
    b3win4 = Polygon(Point(220, 200), Point(250, 200), Point(250, 160), Point(220, 160))
    b3win4.setFill(color_rgb(200, 200, 200))



    b3win5 = Polygon(Point(380, 200), Point(350, 200), Point(350, 160), Point(380, 160))
    b3win5.setFill(color_rgb(200, 200, 200))
    b3win6 = Polygon(Point(380, 220), Point(350, 220), Point(350, 260), Point(380, 260))
    b3win6.setFill(color_rgb(200, 200, 200))
    b3win7 = Polygon(Point(380, 280), Point(350, 280), Point(350, 320), Point(380, 320))
    b3win7.setFill(color_rgb(200, 200, 200))
    b3win8 = Polygon(Point(380, 340), Point(350, 340), Point(350, 380), Point(380, 380))
    b3win8.setFill(color_rgb(255,153,51))

#building 4


    b4 = Polygon(Point(600, 300), Point(400, 300), Point(400, 400), Point(600, 400))
    b4.setFill((color_rgb(34,120, 164)))

    b4win1 = Polygon(Point(420, 320), Point(450, 320), Point(450, 360), Point(420, 360))
    b4win1.setFill(color_rgb(255,153,51))

    b4win5 = Polygon(Point(580, 320), Point(550, 320), Point(550, 360), Point(580, 360))
    b4win5.setFill(color_rgb(255,153,51))



    # building 5
    b5 = Polygon(Point(600, 100), Point(800, 100), Point(800, 400), Point(600, 400))
    b5.setFill((color_rgb(100, 100, 100)))

    b5win1 = Polygon(Point(620, 220), Point(650, 220), Point(650, 260), Point(620, 260))
    b5win1.setFill(color_rgb(200, 200, 200))
    b5win2 = Polygon(Point(620, 280), Point(650, 280), Point(650, 320), Point(620, 320))
    b5win2.setFill(color_rgb(255,153,51))
    b5win3 = Polygon(Point(620, 340), Point(650, 340), Point(650, 380), Point(620, 380))
    b5win3.setFill(color_rgb(255,153,51))
    b5win4 = Polygon(Point(620, 200), Point(650, 200), Point(650, 160), Point(620, 160))
    b5win4.setFill(color_rgb(200, 200, 200))



    b5win5 = Polygon(Point(780, 200), Point(750, 200), Point(750, 160), Point(780, 160))
    b5win5.setFill(color_rgb(255,153,51))
    b5win6 = Polygon(Point(780, 220), Point(750, 220), Point(750, 260), Point(780, 260))
    b5win6.setFill(color_rgb(200, 200, 200))
    b5win7 = Polygon(Point(780, 280), Point(750, 280), Point(750, 320), Point(780, 320))
    b5win7.setFill(color_rgb(200, 200, 200))
    b5win8 = Polygon(Point(780, 340), Point(750, 340), Point(750, 380), Point(780, 380))
    b5win8.setFill(color_rgb(200, 200, 200))



    # building 6
    b6 = Polygon(Point(900, 200), Point(800, 200), Point(800, 400), Point(900, 400))
    b6.setFill((color_rgb(37, 73, 27)))


    b6win2 = Polygon(Point(820, 280), Point(850, 280), Point(850, 320), Point(820, 320))
    b6win2.setFill(color_rgb(200, 200, 200))
    b6win3 = Polygon(Point(820, 340), Point(850, 340), Point(850, 380), Point(820, 380))
    b6win3.setFill(color_rgb(200, 200, 200))
    b6win4 = Polygon(Point(820, 220), Point(850, 220), Point(850, 260), Point(820, 260))
    b6win4.setFill(color_rgb(200, 200, 200))




    #Plane

    planefront = Polygon(Point(390,50),Point(420,35),Point(420,65))
    planefront.setFill(color_rgb(220, 10, 10))
    planebody=Polygon(Point(420,35),Point(470,35), Point(480,25),Point(490,25), Point(490,65),Point(420,65))
    planebody.setFill(color_rgb(255,255,255))
    wing=Polygon(Point(445,50), Point(460,50),Point(460,20),Point(445,20))
    wing.setFill(color_rgb(51,153,255))


    #CAR 1
    car1=Polygon(Point(100,410), Point(120,410),Point(150,380), Point(200,380), Point(230,410),Point(270,420), Point(270,450),Point(100,450))
    car1.setFill(color_rgb(250,0,0))
    a=Point(130, 450)
    car1w1=Circle(a,15)
    car1w1.setFill(color_rgb(100,100,100))
    b=Point(230,450)
    car1w2=Circle(b,15)
    car1w2.setFill(color_rgb(100,100,100))
    car1w2.setWidth(5)
    car1w1.setWidth(5)
    car1.setWidth(1)
    car1.setOutline(color_rgb(0,0,0))
    carwin=Polygon(Point(130,415),Point(220,415),Point(195,390),Point(175,390),Point(175,415),Point(175,390),Point(152,390))
    carwin.setFill(color_rgb(50,50,50))
    carwin.setWidth(2)
    carwin.setOutline(color_rgb(0,0,0))


    #Bus

    bus=Polygon(Point(570,460), Point(800,460),Point(800,570), Point(550,570),Point(550,530))
    bus.setFill(color_rgb(102,102,255))

    door=Polygon(Point(570,490), Point(600,490),Point(600,570), Point(570,570))
    door.setFill(color_rgb(50,50,50))
    p=Point(620, 570)
    busw1=Circle(p,17)
    busw1.setFill(color_rgb(100,100,100))
    q=Point(770,570)
    busw2=Circle(q,17)
    busw2.setFill(color_rgb(100,100,100))
    busw2.setWidth(5)
    busw1.setWidth(5)
    bus.setWidth(2)
    #bus.setOutline(color_rgb(255,255,255))
    buswin1=Polygon(Point(620,470), Point(650,470),Point(650,520),Point(620,520))
    buswin1.setFill(color_rgb(100,100,100))
    buswin1.setWidth(5)
    buswin1.setOutline(color_rgb(0,0,0))
    buswin2=Polygon(Point(660,470), Point(690,470),Point(690,520),Point(660,520))
    buswin2.setFill(color_rgb(100,100,100))
    buswin2.setWidth(5)
    buswin3=Polygon(Point(700,470), Point(730,470),Point(730,520),Point(700,520))
    buswin3.setFill(color_rgb(100,100,100))
    buswin3.setWidth(5)
    buswin4=Polygon(Point(740,470), Point(770,470),Point(770,520),Point(740,520))
    buswin4.setFill(color_rgb(100,100,100))
    buswin4.setWidth(5)



    r=Point(730,570)
    busw3=Circle(r,17)
    busw3.setFill(color_rgb(100,100,100))
    busw3.setWidth(5)

    message = Text(Point(690, 535), "BUBT")
    message.setSize(17)
    message.setTextColor("White")
    message.setStyle("bold")













    road.draw(win)
    b1.draw(win)
    b1win1.draw(win)
    b1win2.draw(win)
    b1win3.draw(win)
    b2.draw(win)
    b2win1.draw(win)
    b2win2.draw(win)
    b2win3.draw(win)
    b2win4.draw(win)
    b2win5.draw(win)
    b2win6.draw(win)
    b2win7.draw(win)
    b2win8.draw(win)
    b3.draw(win)
    b3win1.draw(win)
    b3win2.draw(win)
    b3win3.draw(win)
    b3win4.draw(win)
    b3win5.draw(win)
    b3win6.draw(win)
    b3win7.draw(win)
    b3win8.draw(win)
    b4.draw(win)
    b4win1.draw(win)

    b4win5.draw(win)

    b5.draw(win)
    b5win1.draw(win)
    b5win2.draw(win)
    b5win3.draw(win)
    b5win4.draw(win)
    b5win5.draw(win)
    b5win6.draw(win)
    b5win7.draw(win)
    b5win8.draw(win)

    b6.draw(win)

    b6win2.draw(win)
    b6win3.draw(win)
    b6win4.draw(win)
    roadup.draw(win)
    roaddown.draw(win)
    roadline1.draw(win)
    roadline2.draw(win)
    roadline3.draw(win)
    roadline4.draw(win)
    roadline5.draw(win)
    moon.draw(win)
    planebody.draw(win)

    planefront.draw(win)
    wing.draw(win)
    car1.draw(win)
    car1w1.draw(win)
    car1w2.draw(win)
    bus.draw(win)
    door.draw(win)
    busw1.draw(win)
    busw2.draw(win)
    busw3.draw(win)
    carwin.draw(win)
    buswin1.draw(win)
    buswin2.draw(win)
    buswin3.draw(win)
    buswin4.draw(win)
    message.draw(win)
    field.draw(win)









    win.getMouse()
    win.close()



main()