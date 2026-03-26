// Task 4: List of elements
// Write a JavaScript script that adds a <li> element to a list when the user clicks
// on the element with id add_item
// The new element must be: <li>Item</li>
// The new element must be added to the ul element with class my_list

document.getElementById('add_item').addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
});
