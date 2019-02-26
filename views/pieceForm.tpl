 <form action="/pieces" method="POST">
    <label for="pieceTitle">Titre: </label>
    <input type="text" id="pieceTitle"><br>

    <label for="type">Type: </label>
    <input type="text" id="type"><br>

    <label for="composer">Compositeur: </label>
    <select id="composer">
        <option></option>
        % for item in composersArray:
            <option value={{item}}>{{item}}</option>
        % end
    </select>

    <label for="dateOfCreation">Creation date: </label>
    <input type="date" id="dateOfCreation"><br>

    <label for="difficulty">Difficulty: </label>
    <input type="range" min="1" max="5" id="difficulty">

    <label for="appreciation">Appreciation: </label>
    <input type="range" min="1" max="5" id="appreciation">

    <label for="comments">Comments: </label>
    <input type="text" id="comments"><br>

    <input type="reset" value="Reset">
    <input type="submit">
</form>
