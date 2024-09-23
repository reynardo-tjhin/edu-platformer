const canvas = document.querySelector('canvas');
const c = canvas.getContext('2d');

// define the gameplay's area: canvas' width and height
canvas.width = 64 * 16;
canvas.height = 64 * 9;

console.log("got here! (index.js)");

// define some variables
let parsedCollisions
let collisionBlocks
let background
let doors

// create a player variable
const player = new Player({
    imageSrc: "/static/platformer/images/king/idle.png",
    frameRate: 11,
    animations: { 
        idleRight: {
            frameRate: 11,
            frameBuffer: 2,
            loop: true,
            imageSrc: '/static/platformer/images/king/idle.png',
        },
        idleLeft: {
            frameRate: 11,
            frameBuffer: 2,
            loop: true,
            imageSrc: '/static/platformer/images/king/idleLeft.png',
        },
        runRight: {
            frameRate: 8,
            frameBuffer: 4,
            loop: true,
            imageSrc: '/static/platformer/images/king/runRight.png',
        },
        runLeft: {
            frameRate: 8,
            frameBuffer: 4,
            loop: true,
            imageSrc: '/static/platformer/images/king/runLeft.png',
        },
        enterDoor: {
            frameRate: 8,
            frameBuffer: 4,
            loop: false,
            imageSrc: '/static/platformer/images/king/enterDoor.png', 
            onComplete: () => {
                console.log("completed animation")
                gsap.to(overlay, {
                    opacity: 1,
                    onComplete: () => {
                        document.getElementById("submit").click();
                        level++
                        if (level === 4) level = 1
                        levels[level].init()
                        player.switchSprite('idleRight')
                        player.preventInput = false
                        gsap.to(overlay, {
                            opacity: 0,
                        })
                    }
                })
            }   
        }
    },
});

// Include all items that will change on a level basis
let levels = {
    1: {
        init: () => {
            parsedCollisions = collisionLevel1.parse2D();
            collisionBlocks = parsedCollisions.createObjectsFrom2D();
            player.collisionBlocks = collisionBlocks

            if (player.currentAnimation) player.currentAnimation.isActive = false

            background = new Spirte({
                position: {
                    x: 0,
                    y: 0,
                }, 
                imageSrc: '/static/platformer/images/backgroundLevel1.png',
            })

            doors = [
                new Spirte({
                    position: {
                        x: 781,
                        y: 268,
                    },
                    imageSrc: '/static/platformer/images/doorOpen.png',
                    frameRate: 5,
                    frameBuffer: 5,
                    loop: false,
                    autoplay: false,
                }),
            ]
        }
    },
    2: {
        init: () => {
            parsedCollisions = collisionLevel2.parse2D();
            collisionBlocks = parsedCollisions.createObjectsFrom2D();
            player.collisionBlocks = collisionBlocks
            player.position.x = 96
            player.position.y = 158

            if (player.currentAnimation) player.currentAnimation.isActive = false

            background = new Spirte({
                position: {
                    x: 0,
                    y: 0,
                }, 
                imageSrc: '/static/platformer/images/backgroundLevel2.png',
            })

            doors = [
                new Spirte({
                    position: {
                        x: 772,
                        y: 336,
                    },
                    imageSrc: '/static/platformer/images/doorOpen.png',
                    frameRate: 5,
                    frameBuffer: 5,
                    loop: false,
                    autoplay: false,
                }),
            ]
        }
    },
    3: {
        init: () => {
            parsedCollisions = collisionLevel3.parse2D();
            collisionBlocks = parsedCollisions.createObjectsFrom2D();
            player.collisionBlocks = collisionBlocks
            player.position.x = 752 
            player.position.y = 180

            if (player.currentAnimation) player.currentAnimation.isActive = false

            background = new Spirte({
                position: {
                    x: 0,
                    y: 0,
                }, 
                imageSrc: '/static/platformer/images/backgroundLevel3.png',
            })

            doors = [
                new Spirte({
                    position: {
                        x: 176,
                        y: 334,
                    },
                    imageSrc: '/static/platformer/images/doorOpen.png',
                    frameRate: 5,
                    frameBuffer: 5,
                    loop: false,
                    autoplay: false,
                }),
            ]
        }
    }
}

// create a variable to store the possible key pressed
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

const overlay = {
    opacity: 0
}

// animate the objects
// let bottom = y + height;
function animate() {
    window.requestAnimationFrame(animate);
    
    background.draw()
    // collisionBlocks.forEach(collisionBlock => {
    //     collisionBlock.draw();
    // });

    doors.forEach(door => {
        door.draw();
    });
    player.handleInput(keys);
    player.draw();
    player.update();

    // globalAlpha only applies to whatever inside .save() and .restore()
    c.save()
    c.globalAlpha = overlay.opacity // determines the transparency of c.fillRect()
    c.fillStyle = 'black'
    c.fillRect(0, 0, canvas.width, canvas.height)
    c.restore()
}

// define the user's current level from database
let level = JSON.parse(document.getElementById("current_level").textContent);
console.log("level: " + level);

// main
// start the level and animate
levels[level].init();
animate();


