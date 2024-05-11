import React, { useState } from 'react';

function FileUpload() {
  const [file, setFile] = useState(null);
  const [fileUrl, setFileUrl] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('file', file);

    
      fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData,
      })
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
        setFileUrl(data.file_url)
      }).catch((error) => console.error(error))

      
     }
  

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Upload</button>
      {fileUrl && (
        <div>
          <p>File uploaded successfully!</p>
          <img src={fileUrl} alt="Uploaded File" />
        </div>
      )}
    </div>
  );
}

export default FileUpload;
