class Player extends Spirte{
    constructor({ collisionBlocks = [], imageSrc, frameRate }) {
        super({ imageSrc, frameRate })
        this.position = {
            x: 200,
            y: 200,
        }

        this.velocity = {
            x: 0,
            y: 0,
        }

        this.sides = {
            bottom: this.position.y + this.height
        }
        this.gravity = 1;

        this.collisionBlocks = collisionBlocks;
        console.log(this.collisionBlocks)
    }    

    update() {
        // c.fillStyle = 'rgba(0, 0, 255, 0.3)';
        // c.fillRect(this.position.x, this.position.y, this.width, this.height);
        this.position.x += this.velocity.x;
        
        this.checkHorizontalCollision();
        this.fallDown();
        this.checkVerticalCollision();
    }

    checkHorizontalCollision() {
        for (let i = 0; i < this.collisionBlocks.length; i++) {
            const collisionBlock = this.collisionBlocks[i]
            // if a collision exists
            if (this.position.x <= collisionBlock.position.x + collisionBlock.width && 
                this.position.x + this.width >= collisionBlock.position.x &&
                this.position.y + this.height >= collisionBlock.position.y &&
                this.position.y <= collisionBlock.position.y + collisionBlock.height
            ) {
                // if on x axis going to the left
                if (this.velocity.x < -0) {
                    this.position.x = collisionBlock.position.x + collisionBlock.width + 0.01;
                    break;
                }
                // 
                if (this.velocity.x > 0) {
                    this.position.x = collisionBlock.position.x - this.width - 0.01;
                    break;
                }
            } 
        }
    }

    fallDown() {
        this.velocity.y  += this.gravity;
        this.position.y += this.velocity.y;
    } 

    checkVerticalCollision() {
        for (let i = 0; i < this.collisionBlocks.length; i++) {
            const collisionBlock = this.collisionBlocks[i]
            // if a collision exists
            if (this.position.x <= collisionBlock.position.x + collisionBlock.width && 
                this.position.x + this.width >= collisionBlock.position.x &&
                this.position.y + this.height >= collisionBlock.position.y &&
                this.position.y <= collisionBlock.position.y + collisionBlock.height
            ) {
                if (this.velocity.y < 0) {
                    this.velocity.y = 0;
                    this.position.y = collisionBlock.position.y + collisionBlock.height + 0.01;
                    break;
                }
                // 
                if (this.velocity.y > 0) {
                    this.velocity.y = 0;
                    this.position.y = collisionBlock.position.y - this.height - 0.01;
                    break;
                }
            } 
        }
    }
}
