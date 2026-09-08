#!/usr/bin/env bash
set -euo pipefail

DOMAIN=shotmemory.hajin.xyz
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="$HERE/$DOMAIN.nginx.conf"

if [ -z "$(dig +short "$DOMAIN" A | tail -1)" ]; then
  echo "DNS에 $DOMAIN 레코드가 없다. CNAME hajin.xyz 또는 A 49.171.149.125 를 먼저 추가할 것." >&2
  exit 1
fi

sudo cp "$SRC" "/etc/nginx/sites-available/$DOMAIN"
sudo ln -sf "/etc/nginx/sites-available/$DOMAIN" "/etc/nginx/sites-enabled/$DOMAIN"
sudo nginx -t
sudo systemctl reload nginx
sudo certbot --nginx -d "$DOMAIN" --non-interactive --agree-tos --redirect -m hajin.gwon@designovel.com
sudo nginx -t
sudo systemctl reload nginx
echo "https://$DOMAIN"
