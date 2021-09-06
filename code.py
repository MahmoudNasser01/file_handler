def handle_uploaded_file(f, media_id, collection_name, file_name):
    # handle media_id directory
    if not (BASE_DIR / 'media' / 'media_library' / str(media_id)).exists():
        path = os.path.join(BASE_DIR / 'media' / 'media_library', str(media_id))
        os.mkdir(path)
    if not (BASE_DIR / 'media' / 'media_library' / str(media_id) / collection_name).exists():
        path = os.path.join(BASE_DIR / 'media' / 'media_library' / str(media_id), collection_name)
        os.mkdir(path)
    with open(f'media/media_library/{str(media_id)}/{collection_name}/{file_name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
