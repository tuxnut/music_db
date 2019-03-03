// Display / Hide the forms to add a musicSheet / composer
const toggleForm = () => {
    const element = document.getElementById("form");
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

// Filter musicSheet by title
const sortByInput = () => {
    const input = document.getElementById("search_bar");
    const filter = input.value.toUpperCase();
    const musicSheetTable = document.getElementById("sheetTable")
    const rows = musicSheetTable.getElementsByTagName("tr")

    // loop through table rows, hide the ones that does not match the input
    for (let i = 0; i < rows.length; ++i) {
        const sheetTitle = rows[i].getElementsByTagName("td")[0];
        if (sheetTitle) {
            let titleValue = sheetTitle.textContent || sheetTitle.innerText;
            if (titleValue.toUpperCase().indexOf(filter) > -1) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
}

const quickSort = (array) => {
    if (array.length <= 1) return array;
    const left = [];
    const right = [];
    const pivot = array.shift();
    while (array.length) array[0] < pivot ? left.push(array.shift()) : right.push(array.shift());
    return quickSort(left).concat(pivot).concat(quickSort(right));
}

// Sort the tables by the clicked column - Bubble sort
const sortTable = (column) => {
    const table = document.getElementById('sheetTable');
    const rows = table.getElementsByTagName("tr");

    quicksort(rows);
}

