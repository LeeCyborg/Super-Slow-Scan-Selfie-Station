let capture
function setup() {
    createCanvas(340, 280);
    capture = createCapture(VIDEO);
    capture.size(340, 280);
    capture.hide();
}
// Description of draw
function draw(){
    image(capture, 0, 0, 320, 240);
    filter(INVERT);
    textSize(22);
    fill('yellow');
    text('super', 6, 20);
    fill('white');
    text('slow ', 6, 45);
    fill('tomato');
    text('scan', 6, 70);
    fill('limegreen');
    text('selfie', 6, 95);
    fill('lightpurple');
    text('station', 6, 120);

}

function mousePressed (){ 
    saveCanvas('RSSSTV.png');
}
