% import json
% from DatabaseService import computeScoreName, isScorePresent

<!DOCTYPE html>
<html>
<head>
    <title>Partitions</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    % include('menubar.tpl')

    <h1>Partitions</h1>

    <input type="text" id="search_bar" name="search" placeholder="Search.." oninput="sortByInput()"><br>

    <!-- Button to toggle the form -->
    <button onclick="toggleForm()" class="clickable" ><span>Ajouter une partition</span></button>
    <div style="display:none" id="form" class="formContainer">
        <form action="/scores" method="POST">
            % include('scoreForm.tpl', composersArray=composersArray)     
        </form>
    </div>
    <br>
    <br>
    <div class="containerTable">
        <table id="scoreTable">
            <tr>
                <th></th>
                <th class="clickable" onclick="sortTable(1)">Titre</th>
                <th class="clickable" onclick="sortTable(2)">Compositeur</th>
                <th class="clickable" onclick="sortTable(3)">Type</th>
                <th class="clickable" onclick="sortTable(4)">Date de composition</th>
                <th class="clickable" onclick="sortTable(5)">Difficulté</th>
                <th class="clickable" onclick="sortTable(6)">Appréciation</th>
                <th class="clickable" onclick="sortTable(7)">Commentaires</th>
                <th>Actions</th>
            </tr>
            % for item in musicScoresArray:
            <tr>
                <td>
                % if isScorePresent(item['score_id'], item['title'], item['composer']['commonname']):
                    <a href="sheets/web/viewer.html?file=../{{computeScoreName(item['score_id'], item['title'], item['composer']['commonname'])}}" rel="noopener" target="_blank">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none"/><path d="M15 6H3v2h12V6zm0 4H3v2h12v-2zM3 16h8v-2H3v2zM17 6v8.18c-.31-.11-.65-.18-1-.18-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3V8h3V6h-5z"/></svg>
                    </a>
                % end
                </td>
                <td>{{item['title']}}</td>
                <td>{{item['composer']['commonname']}}</td>
                <td>{{item['type']}}</td>
                <td>{{item['dateofcreation']}}</td>
                <td>{{item['difficulty']}}</td>
                <td>{{item['appreciation']}}</td>
                <td>{{item['comments']}}</td>
                <td>
                    <span class="clickable" onclick="handleEditScore(`{{json.dumps(item, indent=4, sort_keys=True, default=str)}}`)"> <!-- Needs 'default=str' to handle date serialization -->
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="18px" height="18px"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                    </span>
                    <span class="clickable" onclick="handleDeleteScore(`{{item['title']}}`)">
                        <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 0 20 20" width="20"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                    </span>
                </td>
            </tr>
            % end
        </table>
    </div>

    <div id="edit" class="modal">
        <form class="modal-content animate" action="/updateScore" method="POST">
            <div id="editionForm" class="formContainer">
                
                <!-- Hide this (non-modifiable) as the old title is used as key in the back-end -->
                <input type="text" id="key" name="key" style="display:none">
                % include('scoreForm.tpl', composersArray=composersArray)

                <button type="button" onclick="document.getElementById('edit').style.display='none'" class="cancelbtn clickable">Annuler</button>
            </div>
        </form>
    </div>

    <div id="delete" class="modal">
        <form class="modal-content animate" action="/deleteScore" method="POST">
            <div id="deletionForm" class="formContainer">
                
                <!-- Hide this (non-modifiable) as the old title is used as key in the back-end -->
                <input type="text" id="key" name="key" style="display:none">

                Supprimer la partition <span name="namePlaceHolder"></span> ?
                <br>
                <input type="submit" class="clickable">
                <button type="button" onclick="document.getElementById('delete').style.display='none'" class="cancelbtn clickable">Annuler</button>
            </div>
        </form>
    </div>
    <script src="script.js"></script>
</body>
</html>
