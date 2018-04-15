import requests

class Gambles():

    def __init__(self, url='http://localhost:8098'):
        self.url = url

    # List Buckets
    def list_buckets(self, bucket_type=None):
        """Return a list of buckets by type or just all buckets
        Parameters
        ----------
        bucket_type : str
            The type of bucket can be None which will give
            default.

        Returns
        -------
        obj
            json of buckets
        """

        if bucket_type:
            response = requests.get(self.url + '/types/' + bucket_type + '/buckets', params={"buckets": "true"})
        else:
            response = requests.get(self.url+'/buckets',params={"buckets":"true"})

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return "Not Found"
        else:
            return response.status_code,response.text


    # List Keys (Should not be used in production)
    def list_keys(self,bucket,bucket_type=None):
        print("you better not be running this in production!")
        # TODO add option to stream {"key":"stream"}
        if bucket_type:
            response = requests.get(self.url+'/types/'+ bucket_type +'/buckets/'+ bucket +'/keys', params={"keys":"true"})
        else:
            response = requests.get(self.url+'/buckets/'+ bucket +'/keys', params={"keys":"true"})

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code,response.text

    # Get Bucket Properties
    def get_bucket_properties(self,bucket, bucket_type=None):
        """Return properties of a bucket"""
        if bucket_type:
            response = requests.get(self.url+'/types/' + bucket_type + '/buckets/'+ bucket +'/props')
        else:
            response = requests.get(self.url+'/buckets/' + bucket + '/props')

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code,response.text

    # Set Bucket Properties
    def set_bucket_properties(self,bucket,data):
        """Set properties of a bucket"""
        response = requests.put(self.url + '/buckets/' + bucket + '/props', json=data)
        if response.status_code == 204:
            return None
        elif response.status_code == 404:
            return "Not Found"
        else:
            return response.status_code, response.text

    # Reset Bucket Properties
    def reset_bucket_properties(self,bucket):
        """Reset bucket properties n_val and allow_mult back to the default settings."""
        response = requests.delete(self.url+'/buckets/'+ bucket +'/props')
        if response.status_code == 204:
            return None
        elif response.status_code == 404:
            return "Not Found"
        else:
            return response.status_code,response.text

    # Server Related Operations
    def ping(self):
        response = requests.get(self.url + '/ping')
        return response

    def stats(self):
        response = requests.get(self.url + '/stats')
        return response.json()

    def resources(self):
        response = requests.get(self.url + '/')
        # return html list
        # what should be do with this?
        return response.text

    # Object Related Operations
    def fetch(self,bucket, key, bucket_type=None):
        """Reads an object from the specified bucket/key."""
        url = None
        if bucket_type:
            url = self.url + '/types/' + bucket_type + '/buckets/' + bucket + '/keys/'+ key
        else:
            url = self.url + '/buckets/' + bucket + '/keys/'+ key

        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return "Not Found"
        else:
            return response.status_code,response.text

    def get(self,bucket, key, bucket_type = None):
        """Reads an object from the specified bucket/key."""
        return self.fetch(bucket, key, bucket_type)

    def store(self, bucket, data, bucket_type=None, key=None):
        """Stores an object under the specified bucket / key."""
        url = None
        if bucket_type:
            url = self.url+'/types/' + bucket_type + '/buckets/'+ bucket +'/keys'
        else:
            url = self.url+'/buckets/' + bucket + '/keys'

        if key:
            url += "/" + key

        # headers = {
        #     'Content-Type':'application/json',
        #     'X-Riak-Vclock':'my-app/0.0.1',
        #     'X-Riak-Meta-*':'',
        #     'X-Riak-Index-*':'',
        #     'Link:':''
        # }

        response = requests.post(url,json=data,params={"returnbody":"true"})
        good_status_codes = (201,200,204)
        if response.status_code in good_status_codes:
            return response.json()
        else:
            return response.status_code,response.text

    def update(self, bucket, bucket_type=None, key=None):
        """Stores an object under the specified bucket / key."""
        return None

    def delete(self, bucket, bucket_type=None, key=None):
        """delete an object under the specified bucket / key."""
        url = None
        if bucket_type:
            url = self.url+'/types/' + bucket_type + '/buckets/'+ bucket +'/keys'
        else:
            url = self.url+'/buckets/' + bucket + '/keys'

        if key:
            url += "/" + key


        response = requests.delete(url)
        good_status_codes = (201,200,204)
        if response.status_code in good_status_codes:
            return None
        else:
            return response.status_code,response.text