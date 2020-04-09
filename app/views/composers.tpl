% import json

<!DOCTYPE html>
<html>
<head>
    <title>Compositeurs</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    % include('menubar.tpl')

    <h1>Compositeurs</h1>

    <!-- Button to toggle the form -->
    <button onclick="toggleForm()" class="clickable"><span>Ajouter un compositeur</span></button>
    <div style="display:none" id="form" class="formContainer">
        <form action="/composers" method="POST">
            % include('composerForm.tpl')
        </form>
    </div>
    <br>
    <br>
    <div class="containerTable">
        <table id="composerTable">
            <tr>
                <th class="clickable" onclick="sortTableByFamilyName(0)">Nom</th>
                <th class="clickable" onclick="sortTable(1)">Naissance</th>
                <th class="clickable" onclick="sortTable(2)">Décès</th>
                <th class="clickable" onclick="sortTable(3)">Nationalité</th>
                <th class="clickable" onclick="sortTable(4)">Style</th>
                <th>Actions</th>
            </tr>
            % for item in composersArray:
                <tr>
                    <td>
                        <div class="tooltip">
                            {{item['fullname']}}
                            <span class="tooltiptext">{{item['commonname']}}</span>
                        </div>
                    </td>
                    % if item['dateofbirth'] != None:
                        <td>{{item['dateofbirth']}}</td>
                    % else:
                        <td>-</td>
                    % end
                    % if item['dateofdeath'] != None:
                        <td>{{item['dateofdeath']}}</td>
                    % else:
                        <td>-</td>
                    % end
                    <td>{{item['nationality']}}</td>
                    <td>{{item['style']}}</td>
                    <td>
                        <span class="clickable" onclick="handleEditComposer(`{{json.dumps(item, indent=4, sort_keys=True, default=str)}}`)"> <!-- Needs 'default=str' to handle date serialization -->
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="18px" height="18px"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                        </span>
                        <span class="clickable" onclick="handleDeleteComposer(`{{item['commonname']}}`)">
                            <svg xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 0 20 20" width="20"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
                        </span>
                    </td>
                </tr>
            % end
        </table>
    </div>

    <div id="edit" class="modal">
        <form class="modal-content animate" action="/updateComposer" method="POST">
            <div id="editionForm" class="formContainer">
                
                <!-- Hide this (non-modifiable) as the old name is used as key in the back-end -->
                <input type="text" id="key" name="key" style="display:none">
                % include('composerForm.tpl')

                <button type="button" onclick="document.getElementById('edit').style.display='none'" class="cancelbtn clickable">Annuler</button>
            </div>
        </form>
    </div>

    <div id="delete" class="modal">
        <form class="modal-content animate" action="/deleteComposer" method="POST">
            <div id="deletionForm" class="formContainer">
                
                <!-- Hide this (non-modifiable) as the old name is used as key in the back-end -->
                <input type="text" id="key" name="key" style="display:none">

                Supprimer le compositeur <span name="namePlaceHolder"></span> ?
                <br>
                <input type="submit" class="clickable">
                <button type="button" onclick="document.getElementById('delete').style.display='none'" class="cancelbtn clickable">Annuler</button>
            </div>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
