window.addEventListener('keydown', (event) => {
    console.log(event);    
    switch (event.key) {
        // jump
        case 'w':
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