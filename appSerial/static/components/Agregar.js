function Agregar(props)
{
    const idModalWindow = `nuevo${props.nameWindow}`

    return(
        <div className="modal fade" data-bs-backdrop="static" data-bs-keyboard="false" tabIndex="-1" role="dialog" id={idModalWindow}>
            <div className="modal-dialog modal-dialog-centered" role="document">
                <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title">Nuevo {props.nameWindow}</h5>
                        <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div className="modal-body">
                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" className="btn btn-primary">Crear</button>
                    </div>
                </div>
            </div>
        </div>
    );
}