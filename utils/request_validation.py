class RequestValidation:
    def __init__(self, req, required_params_names):
        self.req = req
        self.required_params_names = required_params_names
        self.params = None
        self.message = None
        self.valid = False

    def validate_request(self):
        parameters = {p:self.req.params.get(p) for p in self.required_params_names}

        #List of the required parameters that are not in the query and need to be retrieved from the request body 
        params_names_not_in_query = [p[0] for p in parameters.items() if not p[1]]  

        #If params_not_in_query is empty all the parameters are in the query. Otherwise we need to check the request body
        if len(params_names_not_in_query) > 0:
            try:
                req_body = self.req.get_json()
                assert type(req_body) == dict
            except Exception as e:
                self.message = ", ".join(params_names_not_in_query) + " are not in query and the request body is unvalid "
            else:
                unvalid_params_names = [] #list to keep track of the params that are neither in the query string nor the request body
                for param_name in params_names_not_in_query:
                        parameters[param_name] = req_body.get(param_name)
                        if not parameters[param_name]:
                            unvalid_params_names.append(param_name)

                if len(unvalid_params_names) < 1:
                    self.valid = True
                else:
                    self.message = ", ".join(unvalid_params_names) + " could not be found in query string nor request body. Please provide the missing parameter(s)."
        else:
            self.valid = True

        self.params = parameters