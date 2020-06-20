let board = [['', '', ''], 
             ['', '', ''], 
             ['', '', '']]

let w; 
let h; 

let ai = 'X'; 
let human = 'O'; 
let currentPLayer = human;
            
function setup() { 
    createCanvas(400, 400); 
    w = width / 3; 
    h = height / 3; 
    bestMove()
} 

function equals3(a, b, c) { 
    return a == b && b == c && a != '';
} 

function checkWinner() { 
    let winner = null; 

    for(let i = 0; i < 3; i++) { 
        if(equals3(board[i][0], board[i][1], board[i][2]))  { 
            winner = board[i][0];
        }
    } 

    for(let i = 0; i < 3; i++) { 
        if(equals3(board[0][i], board[1][i], board[2][i])) { 
            winner = board[0][i]
        }
    } 

    if(equals3(board[0][0], board[1][1], board[2][2])) { 
        winner = board[0][0];
    } 

    let openSlots = 0; 
    for(let i = 0; i < 3; i++) { 
        for(let j = 0; j < 3; j++) { 
            if(board[i][j] == '') { 
                openSlots++;
            }
        }
    } 
    if(winner == null && openSpots == 0) { 
        return 'Egal';
    } else {
        return winner;
    }
} 

function mousePressed() { 
    if(currentPLayer == human) { 
        let i = floor(mouseX / w); 
        let j = floor(mouseY / h); 

        if(board[i][j] == '') { 
            board[i][j] = human; 
            currentPLayer = ai; 
            bestMove()
        }
    } 
} 
function draw() { 
    background(255); 
    strokeWeight(4); 

    line(w, 0, w, height); 
    line(w * 2, 0, w * 2, height); 
    line(0, h, width, h); 
    line(0, h * 2, width, h * 2); 

    for(let j = 0; j < 3; j++) { 
        for(let i = 0; i < 3; i++) { 
            let x = w * i + w / 2; 
            let y = h * j + h / 2; 
            let spot = board[i][j]; 
            textSize(32); 
            let r = w / 4; 
            if(spot == human) { 
                noFill() 
                ellipse(x, y, r * 2);
            } else if (spot == ai) { 
                line(x - r, y - r, x + r, y + r); 
                line(x + r, y - r, x - r, y + r);
            }
        }
    } 

    let result = checkWinner(); 
    if(result != null) { 
        noLoop(); 
        let resultP = createP(''); 
        resultP.style('font-size', '32pt'); 
        if(result == 'Egal') { 
            resultP.html('Egal!');
        } else { 
            resultP.html(`${result} a castigat`)
        }
    } 
}
