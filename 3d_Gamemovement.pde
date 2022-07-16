triangulo fig1;
color gris = color(70, 74, 69);
color colorcito = color(70, 74, 69);
color temp;

void setup(){
  size(680, 680, P3D);
  lights();
  fig1 = new triangulo(340, 340, 3);
}

void draw(){
  background(colorcito);
  fig1.move();
  temp = fig1.borderDetecter();
  if (temp != gris){
    colorcito = temp;
  }
}


class triangulo{
  int posY = 340;
  int posX = 340;
  int mult = 3;

  triangulo(int startY, int startX, int multiplo){
    posX = startX;
    posY = startY;
    mult = multiplo;
  }

  void display(){
    translate(posX, posY, 0);
    stroke(255);
    rotateX(PI/2);
    rotateZ(-PI/6);
    noFill();

    beginShape();
    vertex(-100, -100, -100);
    vertex( 100, -100, -100);
    vertex(   0,    0,  100);

    vertex( 100, -100, -100);
    vertex( 100,  100, -100);
    vertex(   0,    0,  100);

    vertex( 100, 100, -100);
    vertex(-100, 100, -100);
    vertex(   0,   0,  100);

    vertex(-100,  100, -100);
    vertex(-100, -100, -100);
    vertex(   0,    0,  100);
    endShape();
  }

  void move(){
    if (keyPressed){
      if (key == 'w'){
        posY -= mult;
      }else if (key == 's'){
        posY += mult;
      }else if (key == 'a'){
        posX -= mult;
      }else if (key == 'd'){
        posX += mult;
      }
    }
    display();
  }

  color borderDetecter(){
    color cl = color(70, 74, 69);
    if(posX >= width){
      posX = width;
      cl = color(163, 0, 122);
    }
    if(posX <= 0){
      posX = 0;
      cl = color(73, 62, 122);
    }
    if(posY >= height){
      posY = height;
      cl = color(90, 84, 73);
    }
    if(posY <= 0){
      posY = 0;
      cl = color(172, 193, 47);
    }
    return cl;
  }

}
