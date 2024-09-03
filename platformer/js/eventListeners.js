window.addEventListener('keydown', (event) => {   
    if (player.preventInput) return
    switch (event.key) {
        // jump
        case 'w':
            for (let i = 0; i < doors.length; i++) {
                const door = doors[i]

                if (
                    player.hitbox.position.x + player.hitbox.width <= door.position.x + door.width && 
                    player.hitbox.position.x  >= door.position.x &&
                    player.hitbox.position.y + player.hitbox.height >= door.position.y &&
                    player.hitbox.position.y  <= door.position.y + door.height
                ) {
                    player.velocity.x, player.velocity.y = 0
                    player.preventInput = true
                    player.switchSprite('enterDoor')
                    door.play()
                    return
                }
            }

            if (player.velocity.y === 0) player.velocity.y = -15;
            break;
        // left
        case 'a':
            keys.a.pressed = true;
            break;
        // down
        case 's':
            break;
        // right
        case 'd':
            keys.d.pressed = true;
            break;

        default:
            break;
    }
})

window.addEventListener('keyup', (event) => {
    console.log(event);    
    switch (event.key) {
        // left
        case 'a':
            keys.a.pressed = false;
            break;
        // right
        case 'd':
            keys.d.pressed = false;
            break;

        default:
            break;
    }
})