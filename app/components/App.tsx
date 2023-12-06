import React, { useState } from "react";
import axios from "axios";
import "./style.css";
// import data from "../Design1";
const App: React.FC = () => {
  const [companyType, setCompanyType] = useState("");
  const [companyName, setCompanyName] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = () => {
    // parent.postMessage({ pluginMessage: { type: "generate", data } }, "*");
    const fetchData = async () => {
      try {
        setLoading(true);
        const { data } = await axios.post(
          "http://127.0.0.1:5000/post",
          {
            variable1: companyType,
            variable2: companyName,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        console.log("--data--", data);
        try {
          const { data } = await axios.get(
            "http://127.0.0.1:5000/get_data"
          );
          console.log("-- get data--", data);
          parent.postMessage(
            { pluginMessage: { type: "generate", data } },
            "*"
          );
        } catch (error) {
          console.log("--get error--", error);
        }
      } catch (error) {
        console.log("--error--", error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  };
  const handleCompanyType = (e: any) => {
    setCompanyType(e.target.value);
    console.log("--company type--", companyType);
  };
  const handleCompanyName = (e: any) => {
    setCompanyName(e.target.value);
    console.log("--company name--", companyName);
  };
  // console.log("--data--", data);
  return (
    <div>
      {/* <h1>Click to generate design</h1>
      <input
        onChange={handleCompanyType}
        placeholder="Enter the company type"
      ></input>
      <input
        onChange={handleCompanyName}
        placeholder="Enter the company name"
      ></input>
      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate"}
      </button> */}
      <center>
        <div className="container">
          <h1>PROMPT2UI</h1>
          <h4>Generate UI landing pages with a single prompt</h4>
          <form>
            <input
              className="form-input"
              type="text"
              placeholder="Industry type"
              onChange={handleCompanyType}
            />
            <br />
            <input
              className="form-input"
              type="text"
              placeholder="Company Name"
              onChange={handleCompanyName}
            />
            <br />
            <button className="btn" onClick={handleGenerate} disabled={loading}>
              ✨ Generate
            </button>
          </form>
        </div>
      </center>
    </div>
  );
};

export default App;
