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

    
      fetch('https://image-to-url-link-testing.onrender.com/upload', {
        method: 'POST',
        body: formData,
      })
      .then((res) => res.json())
      .then((data) => {
        console.log(data.file_url)
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
