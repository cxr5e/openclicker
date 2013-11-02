isEven(val) {
    return val % 2 === 0; 
}

test('isEven()', function() {
    ok(isEven(0), 'Zero is an even number'); 
    ok(isEven(-4), 'Negative four is an even number'); 
    })