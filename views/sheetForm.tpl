 <form action="/sheets" method="POST">
    <label for="title">Titre: </label>
    <input type="text" id="title" name="title"><br>

    <label for="type">Type: </label>
    <input type="text" id="type" name="type"><br>

    <label for="composer">Compositeur: </label>
    <select id="composer" name="composer">
        <option></option>
        % for item in composersArray:
            <option value={{item}}>{{item}}</option>
        % end
    </select>

    <label for="dateOfCreation">Date de composition: </label>
    <input type="date" id="dateOfCreation" name="dateOfCreation"><br>

    <label for="difficulty">Difficulté: </label>
    <input type="range" min="1" max="5" id="difficulty" name="difficulty">

    <label for="appreciation">Appréciation: </label>
    <input type="range" min="1" max="5" id="appreciation" name="appreciation"><br><br>

    <label for="comments">Commentaires: </label>
    <input type="text" id="comments" name="comments"><br>

    <input type="reset" value="Reset">
    <input type="submit">
</form>
