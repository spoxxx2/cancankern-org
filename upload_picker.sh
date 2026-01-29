#!/bin/bash

ACCOUNT="cancanstorageacct01"
CONTAINER="evidence"
BASE_URL="https://$ACCOUNT.blob.core.windows.net/$CONTAINER"
SAS_TOKEN="?se=2027-01-28T00:00Z&sp=rwd&sv=2026-02-06&sr=c&sig=/HEHRbwhyUFVimIG7ssGdT3oPw/55dggNiOp2vTfeoc%3D"

echo "Select a photo from your gallery…"
FILE=$(termux-storage-get)

if [ -z "$FILE" ]; then
    echo "No file selected."
    exit 1
fi

NAME=$(basename "$FILE")

echo "Uploading: $NAME"
echo "DEBUG URL: $BASE_URL/$NAME$SAS_TOKEN"

curl -X PUT \
  -H "x-ms-blob-type: BlockBlob" \
  --data-binary @"$FILE" \
  "$BASE_URL/$NAME$SAS_TOKEN"

echo "Upload complete."
