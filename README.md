# Fast upload image

Fastchymuse

## How it works

-   Upload image to website by cli.
-   Image is sent as base64 data or binary.

## Usage:

```
-h, --help                                                    show this help message and exit
-i IMAGE, --image IMAGE (up to 32 MB)                         define the path to file desire to upload   (Required)
-n NAME, --name NAME                                          define the name of the file                (Optional)
-e EXPIRATION, --expiration EXPIRATION (seconds 60-15552000)  define the expiration time                 (Optional)
```

## Example:

```bash
python3 main.py -i image.png -n thisname -e 3600
```

## Note:

Provided by [ImBB](https://imgbb.com/).
