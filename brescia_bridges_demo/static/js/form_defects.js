$(document).ready(function(jQuery) {
    jQuery(function($) {
        let addRowContainer = $(".add-row")[0];
        addRowContainer.style.cssText='display: none;';
        $("#defects-table-loader").hide();

        //Remove the view, change, and edit of each defect, if present (for the "change" view)
        let existingDefects = $(".field-defect");
        if(existingDefects.length > 0){
            existingDefects.each(function() {
                let fieldDefect = $(this).find(".related-widget-wrapper")[0];
                //remove the other buttons for adding and seeing defects
                $(fieldDefect.children[3]).remove();
                $(fieldDefect.children[2]).remove();
                $(fieldDefect.children[1]).remove();

                let selectField = fieldDefect.children[0];
                //"lock" the field
                selectField.setAttribute('readonly', true);
                $(selectField).mousedown(function(e){
                    e.preventDefault();
                });
            });
        }

        $('select#id_piece').on('change', (event) => {
            let selected = event.target.value;
            let url = '/api/related_answers_for_piece?piece_id=' + selected;
            let rowClass = ".dynamic-formdefectsanswer_set";
            let addedRows = $(rowClass);
            addedRows.remove();

            let pieceIdSelect = $("select#id_piece")[0];
            pieceIdSelect.disabled = true;

            $("#defects-table-loader").show();
            $.getJSON(url, function (data) {
                //In case there are still rows added 
                let addedRows = $(rowClass);
                addedRows.remove(); 

                let pieceIdSelect = $("select#id_piece")[0];
                pieceIdSelect.disabled = false;

                $("#defects-table-loader").hide();
                if(data){
                    for(let i in data){
                        addRowContainer.children[0].children[0].click();
                        let newAddedRow = $(rowClass)[i];
                        //Remove the delete button
                        $(newAddedRow).find(".inline-deletelink").remove();
                        
                        //Find the field defect
                        let fieldDefect = $(newAddedRow).find(".related-widget-wrapper")[0];
                        let selectField = fieldDefect.children[0];

                        //remove the other buttons for adding and seeing defects
                        $(fieldDefect.children[3]).remove();
                        $(fieldDefect.children[2]).remove();
                        $(fieldDefect.children[1]).remove();

                        //Defect G value
                        let gValue = data[i].fields.g;
                        let psSelect = $(newAddedRow).find(".field-ps")[0].children[0];
                        let gField = $(newAddedRow).find(".field-defect_g")[0].children[0];
                        gField.innerHTML = gValue;

                        if(gValue < 4){
                            //Hide the PS field if G is less than 4
                            psSelect.setAttribute('hidden', 'hidden');
                        } else {
                            //Remove the "None" option if G is 4 or 5
                            $(psSelect).find("[value|=None]")[0].remove();
                            $(psSelect).find("[value|=NO]")[0].setAttribute('selected', '');;
                        }

                        //Put the select value and "lock" the field
                        selectField.value = data[i].pk;
                        selectField.setAttribute('readonly', true);
                        $(selectField).mousedown(function(e){
                            e.preventDefault();
                        });

                    }
                    addRowContainer.style.cssText='display: none';
                }
                
            });

        });
    });
});
