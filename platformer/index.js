const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d');

canvas.width = 64 * 16;
canvas.height = 64 * 9;


const parsedCollisions = collisionLevel1.parse2D();
const collisionBlocks = parsedCollisions.createObjectsFrom2D();

const backgroundLevel1 = new Spirte({
    position: {
        x: 0,
        y: 0,
    }, 
    imageSrc: './Assets/img/backgroundLevel1.png',
})

const player = new Player({
    collisionBlocks,
    imageSrc: './Assets/img/king/idle.png',
    frameRate: 11,
    animations: {
        idleRight: {
            frameRate: 11,
            frameBuffer: 2,
            loop: true,
            imageSrc: './Assets/img/king/idle.png',
        },
        idleLeft: {
            frameRate: 11,
            frameBuffer: 2,
            loop: true,
            imageSrc: './Assets/img/king/idleLeft.png',
        },
        runRight: {
            frameRate: 8,
            frameBuffer: 4,
            loop: true,
            imageSrc: './Assets/img/king/runRight.png',
        },
        runLeft: {
            frameRate: 8,
            frameBuffer: 4,
            loop: true,
            imageSrc: './Assets/img/king/runLeft.png',
        },
    },
});

const doors = [
    new Spirte({
        position: {
            x: 0,
            y: 0,
        },
        imageSrc: './Assets/img/doorOpen.png',
        frameRate: 5,
        frameBuffer: 5,
        loop: false,
    }),
]

const keys = {
    w: {
        pressed: false
    },
    a: {
        pressed: false
    },
    d: {
        pressed: false
    },
}


// let bottom = y + height;
function animate() {
    window.requestAnimationFrame(animate);
    
    backgroundLevel1.draw()
    collisionBlocks.forEach(collisionBlock => {
        collisionBlock.draw();
    });

    doors.forEach(door => {
        door.draw();
    });
    

    player.velocity.x = 0;
    if (keys.d.pressed) {
        player.switchSprite('runRight')
        player.velocity.x = 5 
        player.lastDirection = 'right'
    } else if (keys.a.pressed) {
        player.switchSprite('runLeft')
        player.velocity.x = -5;
        player.lastDirection = 'left'
    } else {
        if (player.lastDirection === 'left') player.switchSprite('idleLeft')
        else player.switchSprite('idleRight')
    }
    player.draw();
    player.update()
}

animate();


