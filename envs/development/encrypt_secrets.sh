gpg --symmetric --cipher-algo AES256 .secrets
echo "REMEMBER TO SET THIS PASSWORD ON GITHUB SECRETS BEFORE COMMITING"

# to decrypt
# gpg --quiet --batch --yes --decrypt --passphrase="${{ secrets.SECRETS_ENCRYPTION_KEY }}" --output .secrets .secrets.gpg
