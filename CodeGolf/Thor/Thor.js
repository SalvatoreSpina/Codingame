// Readable version

[x,y,X,Y]=readline().split(' ')
for(;;){
    print((y>Y++?"S":y<--Y?(Y--,"N"):"") + (x>X++?"E":x<--X?(X--,"W"):""))
}

// Code Golf

[x,y,X,Y]=readline().split(' ');for(;;){print((y>Y++?"S":y<--Y?(Y--,"N"):"")+(x>X++?"E":x<--X?(X--,"W"):""))}