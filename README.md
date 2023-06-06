# tk-framework-dropbox

This is a Dropbox Toolkit framework that provides basic uploading and downloading files to and from a cloud storage solution.

## Usage

The framework contains a simple API interface for uploading and downloading files.
Once the framework has been added to your config, you can import it within your hooks.
Assuming you defined your framework instance name as `tk-framework-dropbox_v1.x.x`, you can import it as follows:

```python
remote_storage = self.load_framework("tk-framework-dropbox_v1.x.x")
```

The framework has two public methods that can be called:

#### `upload_publish(published_file)`
This expects a ShotGrid `PublishedFile` entity dictionary, and will upload the file path associated with that entity to dropbox.
It returns a `str` path to the uploaded file.

#### `upload_publishes(published_files)`
A convenience method based on the `upload_publish`, which can be passed a list of `PublishedFile` entities.
This returns a list of paths to the uploaded files.

#### `download_publish(published_file)`

This expects a ShotGrid `PublishedFile` entity dictionary, and will download the file associated with that entity. The location it will be downloaded to can be implemented via the hooks.
It returns a `str` path to the downloaded file.

#### `download_publishes(published_files)`

A convenience method based on the `download_publish`, which can be passed a list of `PublishedFile` entities.
This returns a list of paths to the downloaded files.

## Configuration

Framework provides default `upload()` and `download()` methods functionality via `hook_provider`, up to you to take over the hook and override its generic behaviour.
