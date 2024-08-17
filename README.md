# Accessing Kaggle datasets via API

This workflow allows us to access Kaggle datasets via API, instead of manual downloads, which is time-consuming, and avoid storage for heavy files locally.

##### Steps to setup Kaggle API

Change current directory to the kaggle directory.
```
cd /users/kramchurn/.kaggle
```

Create new directory called kaggle
```
mkdir -/.kaggle
```

Create API token from Kaggle and download json file and move the file to the newly created Kaggle directory.

```
cp /users/kramchurn/Downloads/kaggle.json /users/kramchurn/.kaggle/kaggle.json
```

List directory (ls)


Look for other datasets
```
kaggle datasets list
```
