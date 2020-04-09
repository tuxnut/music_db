const s_titleColumn          = 1;
const s_composerNameColumn   = 2;
const s_typeColumn           = 3;
const s_creationDateColumn   = 4;
const s_difficultyColumn     = 5;
const s_appreciationColumn   = 6;
const s_commentColumn        = 7;
const s_actionColumn         = 8;

const c_fullNameColum        = 0;
const c_birthColum           = 1;
const c_deathColum           = 2;
const c_nationalityColum     = 3;
const c_styleColum           = 4;
const c_actionColumn         = 5;

// Display / Hide the forms to add a musicScore / composer
const toggleForm = () => {
    const element = document.getElementById("form");
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

// Filter musicScore by title and or composer
const sortByInput = () => {
    const input = document.getElementById("search_bar");
    const filter = input.value.toUpperCase();
    const musicScoreTable = document.getElementById("scoreTable")
    const rows = musicScoreTable.getElementsByTagName("tr")

    // loop through table rows, hide the ones that does not match the input
    for (let i = 0; i < rows.length; ++i) {
        const scoreTitle = rows[i].getElementsByTagName("td")[s_titleColumn];
        const composerName = rows[i].getElementsByTagName("td")[s_composerNameColumn];
        if (scoreTitle && composerName) {
            let titleValue = scoreTitle.textContent || scoreTitle.innerText;
            let composerNameValue = composerName.textContent || composerName.innerText;
            if ((titleValue.toUpperCase().indexOf(filter) > -1) || (composerNameValue.toUpperCase().indexOf(filter) > -1)) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
}

const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;

const comparer = (idx, asc) => (a, b) => ((v1, v2) => 
    v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
)(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));
    
// Sort the tables by the clicked column - Bubble sort
const sortTable = (column) => {
    const page = document.getElementsByTagName("title")[0].textContent;
    const table = document.getElementById((page === "Partitions") ? "scoreTable" : "composerTable");
    Array.from(table.querySelectorAll('tr:nth-child(n+2)'))
    .sort(comparer(column, this.asc = !this.asc))
    .forEach(tr => table.appendChild(tr));
}

const getFamilyName = (tr, idx) => {
    content = tr.children[idx].innerText || tr.children[idx].textContent;
    const split = content.split(' ');
    return split[split.length - 1];
}

const comparerByName = (idx, asc) => (a, b) => ((v1, v2) => 
    v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
)(getFamilyName(asc ? a : b, idx), getFamilyName(asc ? b : a, idx));

const sortTableByFamilyName = (column) => {
    const page = document.getElementsByTagName("title")[0].textContent;
    const table = document.getElementById((page === "Partitions") ? "scoreTable" : "composerTable");
    Array.from(table.querySelectorAll('tr:nth-child(n+2)'))
        .sort(comparerByName(column, this.asc = !this.asc))
        .forEach(tr => table.appendChild(tr));
}

const handleEditComposer = (serializedItem) => {
    composer = JSON.parse(serializedItem);
    const container = document.getElementById('editionForm');
    
    container.children.namedItem('key').value = composer.commonname;
    container.children.namedItem('name').value = composer.commonname;    
    container.children.namedItem('fullname').value = composer.fullname;
    container.children.namedItem('dateOfBirth').value = composer.dateofbirth;
    container.children.namedItem('dateOfDeath').value = composer.dateofdeath;
    container.children.namedItem('nationality').value = composer.nationality;
    container.children.namedItem('style').value = composer.style;

    document.getElementById('edit').style.display ='block';
}

const handleDeleteComposer = (itemName) => {
    const container = document.getElementById('deletionForm');
    
    container.children.namedItem('namePlaceHolder').textContent = itemName;
    container.children.namedItem('key').value = itemName;

    document.getElementById('delete').style.display ='block';
}


const handleEditScore = (serializedItem) => {
    musicScore = JSON.parse(serializedItem);
    const container = document.getElementById('editionForm');
    
    container.children.namedItem('key').value = musicScore.title;
    container.children.namedItem('title').value = musicScore.title;
    container.children.namedItem('type').value = musicScore.type;
    container.children.namedItem('composerName').value = musicScore.composer.commonname
    container.children.namedItem('dateOfCreation').value = `${musicScore.dateofcreation}-01-01`;
    container.children.namedItem('difficulty').value = musicScore.difficulty;
    container.children.namedItem('appreciation').value = musicScore.appreciation;
    container.children.namedItem('comments').value = musicScore.comments;
    
    document.getElementById('edit').style.display ='block';
}

const handleDeleteScore = (itemTitle) => {
    const container = document.getElementById('deletionForm');
    
    container.children.namedItem('namePlaceHolder').textContent = itemTitle;
    container.children.namedItem('key').value = itemTitle;

    document.getElementById('delete').style.display ='block';
}

// Get the modals
const modalEdit = document.getElementById('edit');
const modalDelete = document.getElementById('delete');

// When the user clicks anywhere outside of the modals, close it
window.onclick = (event) => {
    if ((event.target == modalEdit) || (event.target == modalDelete)) {
        modal.style.display = "none";
    }
}
