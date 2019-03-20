echo "Are you running this script from the scripts folder? y/n"
read ans
if [ ${ans} == 'y' ]; then
    echo "Retrieving last version"
    git clone git@github.com:Semantic-Org/Semantic-UI.git
    cd ../assets
    git rm -r semantic-ui
    cp -r ../scripts/Semantic-UI/dist semantic-ui
    git add semantic-ui
    cd ../scripts
    rm -rf Semantic-UI
    echo "Done"
fi
