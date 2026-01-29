#!/bin/bash

ACCOUNT="cancanstorageacct01"
CONTAINER="evidence"
BASE_URL="https://$ACCOUNT.blob.core.windows.net/$CONTAINER"
SAS_TOKEN="?se=2027-01-28T00%3A00Z&sp=rwd&sv=2026-02-06&sr=c&sig=/HEHRbwhyUFVimIG7ssGdT3oPw/55dggNiOp2vTfeoc%3D"

GALLERY="/sdcard/DCIM/Camera"

echo "Your gallery contains:"
ls "$GALLERY" | grep -E "\.jpg|\.jpeg|\.png"

echo
echo "Type the exact filenames you want to upload, separated by spaces:"
read -r FILES

for NAME in $FILES; do
    FILE="$GALLERY/$NAME"

    if [ ! -f "$FILE" ]; then
        echo "Skipping: $NAME (not found)"
        continue
    fi

    echo "Uploading: $NAME"
    echo "DEBUG URL: $BASE_URL/$NAME$SAS_TOKEN"

    curl -X PUT \
      -H "x-ms-blob-type: BlockBlob" \
      --data-binary @"$FILE" \
      "$BASE_URL/$NAME$SAS_TOKEN"
done

echo "Gallery upload complete."
