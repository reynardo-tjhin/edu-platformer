// create new method for default Array objects
Array.prototype.parse2D = function() {
    const rows = [];
    // Each row 16 cells
    for (let i=0; i < this.length; i+=16) {
        rows.push(this.slice(i, i+16));
    }
    return rows;
}

Array.prototype.createObjectsFrom2D = function () {
    const objects = []
    this.forEach((row, y) => {
        row.forEach((element, x) => {
           if (element === 292) {
            // push new collision into collisionblocks array
            objects.push(
                new CollisionBlock({
                    position: {
                        x: x * 64,
                        y: y * 64,
                    },
                })
            )
           }
        });
    }); 
    return objects;
}