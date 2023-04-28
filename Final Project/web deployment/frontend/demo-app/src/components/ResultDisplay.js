function ResultDisplay(props) {
    return (
        <table id="result">
            <tr>
                <th>Model</th>
                <th>Prediction</th>
            </tr>

            {
                props.model_names.map((item, id) => (
                    <tr key={id}>
                        <td>{item.name}</td>
                        {item.pred == 0 &&
                            <td>Negative</td>
                        }
                        {item.pred == 1 &&
                            <td>Positive</td>
                        }

                    </tr>
                ))
            }
        </table>
    )
}

export default ResultDisplay;